#startlette stuff
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException
import uvicorn
#malwareconfig stuff
from malwareconfig import fileparser
from malwareconfig.modules import __decoders__, __preprocessors__
#general imports
from os import path

dockerotools = Starlette(debug=True)
SAMPLEPATH="/data/badshit/"

##exception handlers
@dockerotools.exception_handler(404)
async def not_found(request, exc):
    return JSONResponse({"detail": exc.detail}, status_code=exc.status_code)
@dockerotools.exception_handler(412)
async def teapot(request, exc):
    return JSONResponse({"detail": "I'm a little teapot, short and stout. Here is my handle, here is my spount. When I get all steamed up, Hear me shout. Tip me over and pour me out."}, status_code=exc.status_code)
@dockerotools.exception_handler(500)
async def server_error(request, exc):
    return JSONResponse({"detail": exc.detail}, status_code=exc.status_code)

##routes
@dockerotools.route('/')
async def homepage(request):
    return JSONResponse({'hello': 'don\'t just sit there and send me some info @malwareconfig endpoint.'})

@dockerotools.route('/malwareconfig/{filename}')
async def malconf(request):
    filepath=SAMPLEPATH + request.path_params['filename']
    if path.exists(filepath):
        file_info=fileparser.FileParser(file_path=filepath)
        if file_info.malware_name in __decoders__:
            module = __decoders__[file_info.malware_name]['obj']()
            module.set_file(file_info)
            module.get_config()
            conf = module.config
            conf.update({'mal_family': file_info.malware_name})
            return JSONResponse({'config': conf})
        else:
            #raise if we couldn't find any config extractor
            raise HTTPException(status_code=412)
    else:
        #raise if we couldn't find the file in the OS
        raise HTTPException(status_code=404)

if __name__ == '__main__':
    uvicorn.run(dockerotools, host='0.0.0.0', port=8000)