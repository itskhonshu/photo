import pickle

dictionary = {
' : ' : '0',
' Output image format ( png/jpg ?:help ) : ' : 'png',
'Override' : '0',
'[n] Enable gradient clipping ( y/n ?:help ) : ' : 'False',
' Use saved session? ' : 'False',
'[n] Enable pretraining mode ( y/n ?:help ) : ' : 'False',
' Press enter in 2 seconds to override model settings.  ' : '\n',
'[0] Which GPU indexes to choose? : ' : '0',
'[wf] Face type ( f/wf/head ?:help ) : ' : 'wf',
'[0] Max number of faces from image ( ?:help ) : ' : '0',
'[512] Image size ( 256-2048 ?:help ) : ' : '512',
'[90] Jpeg quality ( 1-100 ?:help ) : ' : '90',
'[n] Write debug images to aligned_debug? ( y/n ) : ' : 'False',
'[y] Continue extraction? ( y/n ?:help ) : ' : 'True',
'[2] Autobackup every N hour ( 0..24 ?:help ) : ' : '2',
'[n] Write preview history ( y/n ?:help ) : ' : 'False',
'[83000] Target iteration : ' : '\n',
'[n] Flip SRC faces randomly ( y/n ?:help ) : ' : 'False',
'[n] Flip DST faces randomly ( y/n ?:help ) : ' : 'False',
'[4] Batch_size ( ?:help ) : ' : '4',
'[n] Eyes and mouth priority ( y/n ?:help ) : ' : 'False',
'[y] Uniform yaw distribution of samples ( y/n ?:help ) : ' : 'True',
'[n] Blur out mask ( y/n ?:help ) : ' : 'False',
'[y] Place models and optimizer on GPU ( y/n ?:help ) : ' : 'True',
'[y] Use AdaBelief optimizer? ( y/n ?:help ) : ' : 'True',
'[n] Use learning rate dropout ( n/y/cpu ?:help ) : ' : 'n',
'[y] Enable random warp of samples ( y/n ?:help ) : ' : 'True',
'[0.0] Random hue/saturation/light intensity ( 0.0 .. 0.3 ?:help ) : ' : '0.0',
'[0.0] GAN power ( 0.0 .. 5.0 ?:help ) : ' : '0.0',
'[0.0] Face style power ( 0.0..100.0 ?:help ) : ' : '0.0',
'[0.0] Background style power ( 0.0..100.0 ?:help ) : ' : '0.0',
'[lct] Color transfer for src faceset ( none/rct/lct/mkl/idt/sot ?:help ) : ' : 'lct',
'[n] Use interactive merger? ( y/n ) : ' : 'n',
'[1] 2 : ' : '1',
'[1] 3 : ' : '4',
'[0] Choose erode mask modifier ( -400..400 ) : ' : '100',
'[0] Choose blur mask modifier ( 0..400 ) : ' : '150',
'[0] Choose motion blur power ( 0..100 ) : ' : '0',
'[0] Choose output face scale modifier ( -50..50 ) : ' : '0',
'[0] 1 ( ?:help ) : ' : '0',
'[0] Choose super resolution power ( 0..100 ?:help ) : ' : '0',
'[0] Choose image degrade by denoise power ( 0..500 ) : ' : '0',
'[0] Choose image degrade by bicubic rescale power ( 0..100 ) : ' : '0',
'[0] Degrade color power of final image ( 0..100 ) : ' : '0',
'Color transfer to predicted face ( rct/lct/mkl/mkl-m/idt/idt-m/sot-m/mix-m ) : ' : 'rct',
'[8] Number of workers? ( 1-8 ?:help ) : ' : '8',
'[16] Bitrate of output file in MB/s : ' : '16',
}
with open('/home/deepfake/interact_dict.pkl', 'wb') as handle:
	pickle.dump(dictionary, handle, protocol=4)

with open('/home/deepfake/interact_dict.pkl', 'rb') as handle:
	d = pickle.load(handle)
s = "Use saved"
res = dict(filter(lambda item: s in item[0], d.items()))

print(list(res.values())[0])