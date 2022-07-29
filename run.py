import argparse
import os
from pathlib import Path

ROOT = Path('./')
YOLOv5_PATH = os.path.join(ROOT, 'yolov5')
DETECT_FILE_PATH = os.path.join(YOLOv5_PATH, 'detect.py')
BEST_PT_PATH = os.path.join(ROOT, 'best.pt')
OUTPUTS_PATH = ROOT / 'outputs/'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', default='yolov5s', help='weights to use for the model. best.pt by default')
    parser.add_argument('--source', default=ROOT / 'data/images/', help='path to image or video to detect')
    parser.add_argument('--output-dir', default=ROOT / 'outputs/', help='path to place model output')
    parser.add_argument('--name', default='exp', help='name of folder inside outputs')
    parser.add_argument('--view-img', default=False, action='store_true', help='show results on a seperate viewer')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='confidence threshold. 0.25 by default')
    parser.add_argument('--iou-thres', type=float, default=0.45, help='NMS IoU threshold. 0.45 by default')
    parser.add_argument('--max-det', type=int, default=1000, help='maximum detections per image')
    parser.add_argument('--nosave', action='store_true', help='do not save images/videos')
    parser.add_argument('--device', default='cpu', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')    

    args = parser.parse_args()
    
    view_img = ''
    if args.view_img is True:
        view_img = '--view-img'
    
    nosave = ''
    if args.nosave is True:
        nosave = '--no-save'
    
    command = 'python {} --weights "{}" --source "{}" --project "{}" --name "{}" {} \
    --conf-thres {} --iou-thres {} --max-det {} {} --device {}'.format(DETECT_FILE_PATH, 
                                                                        BEST_PT_PATH,  
                                                                        args.source, 
                                                                        args.output_dir, 
                                                                        args.name, 
                                                                        view_img,
                                                                        args.conf_thres,
                                                                        args.iou_thres, 
                                                                        args.max_det, 
                                                                        nosave, 
                                                                        args.device
                                                                        )
    
    os.system(command)
    
if __name__ == '__main__':
    main()