#startlette stuff
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException
import uvicorn
#malwareconfig stuff
from malwareconfig import fileparser
from malwareconfig.modules import __decoders__, __preprocessors__
#general imports
import os
from os import path
import shutil
import json
from subprocess import DEVNULL, STDOUT, check_call, check_output


dockerotools = Starlette(debug=True)
SAMPLEPATH="/data/badshit/"
DECODERS=['kevin'] #,'jurg']
DECODERSPATH='/opt/decoders/'

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

@dockerotools.route('/malwareconfig/{filename:path}')
async def malconf(request):
    filepath=SAMPLEPATH + request.path_params['filename']
    if path.exists(filepath):
        for package in DECODERS:
            if package == 'kevin':
                file_info=fileparser.FileParser(file_path=filepath)
                if file_info.malware_name in __decoders__:
                    module = __decoders__[file_info.malware_name]['obj']()
                    module.set_file(file_info)
                    module.get_config()
                    conf = module.config
                    conf.update({'mal_family': file_info.malware_name})
                    return JSONResponse({'config': conf})
                # else:
                #     #raise if we couldn't find any config extractor
                #     raise HTTPException(status_code=412)
            elif package == 'jurg':
                # move file to tmp
                if not os.path.exists(os.path.dirname('/tmp/'+request.path_params['filename'])):
                    os.makedirs(os.path.dirname('/tmp/'+request.path_params['filename']))
                shutil.copyfile(filepath,'/tmp/'+request.path_params['filename'])
                # execute qrypter
                check_call(['python3', DECODERSPATH+'java_malware_tools-master/unpackers/qrypter/current-qrypter.py', '/tmp/'+request.path_params['filename']], stdout=DEVNULL, stderr=DEVNULL)
                # check if we have the unpacked file
                if path.exists('/tmp/'+request.path_params['filename']+'.unpacked.jar'):
                    conf=json.loads(check_output(['python3', DECODERSPATH+'java_malware_tools-master/config-extraction/qealler_config.py', '/tmp/'+request.path_params['filename']+'.unpacked.jar']).decode('utf-8'))
                    conf.update({'mal_family': 'qealler'})
                    os.remove('/tmp/'+request.path_params['filename'])
                    os.remove('/tmp/'+request.path_params['filename']+'.unpacked.jar')
                    return JSONResponse({'config': conf})
                else:
                    #raise if we couldn't find the unpacked file
                    raise HTTPException(status_code=412)
            else:
                #raise if we couldn't find any config extractor
                raise HTTPException(status_code=412)
    else:
        #raise if we couldn't find the file in the OS
        raise HTTPException(status_code=404)

if __name__ == '__main__':
    uvicorn.run(dockerotools, host='0.0.0.0', port=8000)
