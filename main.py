from detectron2.demo import demo


def main():

    input_path = './input'
    mask_path = './mask'
    demo.main(input_path,mask_path)