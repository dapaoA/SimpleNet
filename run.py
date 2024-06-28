import os
import subprocess

def main():
    datapath = "C:\\Users\\hokop\\Documents\\GitHub\\SimpleNet\\data\\MVTec-AD"
    datasets = ['screw']

    dataset_flags = ' '.join([f'-d {dataset}' for dataset in datasets])

    command = f"""
    python main.py ^
    --gpu 0 ^
    --seed 0 ^
    --log_group simplenet_mvtec ^
    --log_project MVTecAD_Results ^
    --results_path results ^
    --run_name run ^
    net ^
    -b wideresnet50 ^
    -le layer2 ^
    -le layer3 ^
    --pretrain_embed_dimension 1536 ^
    --target_embed_dimension 1536 ^
    --patchsize 3 ^
    --meta_epochs 8 ^
    --embedding_size 256 ^
    --gan_epochs 4 ^
    --noise_std 0.015 ^
    --dsc_hidden 1024 ^
    --dsc_layers 2 ^
    --dsc_margin .5 ^
    --pre_proj 1 ^
    dataset ^
    --batch_size 8 ^
    --resize 329 ^
    --imagesize 288 {dataset_flags} mvtec {datapath}
    """

    # Remove line breaks for Windows shell compatibility
    command = ' '.join(command.split())

    subprocess.run(command, shell=True)

if __name__ == "__main__":
    main()
