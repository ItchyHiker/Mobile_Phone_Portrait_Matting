import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--model_name', type=str, default='SegNet',\
    help='the model you choose between PrismaNet, PrimaMattingNet')
parser.add_argument('--image_size', type=int, default=224, help='the height / width of the input image to network')
parser.add_argument('--num_classes', type=int, default=2, help='number of model output channels')
parser.add_argument('--batch_size', type=int, default=32, help='batch size')
parser.add_argument('--epoch', type=int, default=100, help='number of epochs to train for')
parser.add_argument('--decay_epoch', type=int, default=10, help='learning rate decay start epoch num')
parser.add_argument('--lr', type=float, default=0.0001, help='learning rate')
parser.add_argument('--sample_step', type=int, default=50, help='step of saving sample images')
parser.add_argument('--checkpoint_step', type=int, default=100, help='step of saving checkpoints')
parser.add_argument('--data_path', default='/home/ubuntu/dataset/portrait', help='path to dataset')
parser.add_argument('--checkpoint_dir', default='checkpoints', help="path to saved models (to continue training)")
parser.add_argument('--sample_dir', default='samples', help='folder to output images and model checkpoints')
parser.add_argument('--workers', type=int, default=4, help='number of data loading workers')
parser.add_argument('--mode', type=str, default='train', help='Trainer mode: train or test')
parser.add_argument('--nf', type=int, default=32, help='The number of filter')
parser.add_argument('--num_test', type=int, default=320, help='The number of test image')
parser.add_argument('--test_result_path', type=str, default='imgs/result', help='The dir for test result')
parser.add_argument('--test_data_path', type=str, default='imgs/test', help='The dir for test imgs')
parser.add_argument('--test_model_path', type=str, default='./models/PrismaNet_portrait_epoch-0099.pth', help='Test model file')

def get_config():
    return parser.parse_args()
