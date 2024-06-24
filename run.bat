@echo off

setlocal EnableDelayedExpansion

rem Set relative path to the data directory
set datapath= C:\Users\hokop\Documents\GitHub\SimpleNet\data\MVTec-AD

rem Define datasets
set datasets=screw

rem Initialize dataset flags
set dataset_flags=
for %%d in (%datasets%) do (
    set dataset_flags=!dataset_flags! -d %%d
)

rem Run the Python script with the specified arguments
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
--meta_epochs 40 ^
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
--imagesize 288 %dataset_flags% mvtec %datapath%

endlocal
