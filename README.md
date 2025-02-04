# Pelatihan Pengenalan DS untuk SWE

## Setup Conda Environment

```sh

C:\Users\username>conda env list

# conda environments:
#
base                   D:\Programs\Programming\miniconda3


C:\Users\username>conda create -n pelatihan python=3.12
Retrieving notices: done
Channels:
 - defaults
Platform: win-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: D:\Programs\Programming\Envs\pelatihan

  added / updated specs:
    - python=3.12


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    ca-certificates-2024.12.31 |       haa95532_0         129 KB
    expat-2.6.4                |       h8ddb27b_0         257 KB
    pip-25.0                   |  py312haa95532_0         3.0 MB
    python-3.12.8              |       h14ffc60_0        16.4 MB
    setuptools-75.8.0          |  py312haa95532_0         2.2 MB
    tzdata-2025a               |       h04d1e81_0         117 KB
    vc-14.40                   |       haa95532_2          10 KB
    vs2015_runtime-14.42.34433 |       h9531ae6_2         1.2 MB
    wheel-0.45.1               |  py312haa95532_0         177 KB
    ------------------------------------------------------------
                                           Total:        23.5 MB

The following NEW packages will be INSTALLED:

  bzip2              pkgs/main/win-64::bzip2-1.0.8-h2bbff1b_6
  ca-certificates    pkgs/main/win-64::ca-certificates-2024.12.31-haa95532_0
  expat              pkgs/main/win-64::expat-2.6.4-h8ddb27b_0
  libffi             pkgs/main/win-64::libffi-3.4.4-hd77b12b_1
  openssl            pkgs/main/win-64::openssl-3.0.15-h827c3e9_0
  pip                pkgs/main/win-64::pip-25.0-py312haa95532_0
  python             pkgs/main/win-64::python-3.12.8-h14ffc60_0
  setuptools         pkgs/main/win-64::setuptools-75.8.0-py312haa95532_0
  sqlite             pkgs/main/win-64::sqlite-3.45.3-h2bbff1b_0
  tk                 pkgs/main/win-64::tk-8.6.14-h0416ee5_0
  tzdata             pkgs/main/noarch::tzdata-2025a-h04d1e81_0
  vc                 pkgs/main/win-64::vc-14.40-haa95532_2
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.42.34433-h9531ae6_2
  wheel              pkgs/main/win-64::wheel-0.45.1-py312haa95532_0
  xz                 pkgs/main/win-64::xz-5.4.6-h8cc25b3_1
  zlib               pkgs/main/win-64::zlib-1.2.13-h8cc25b3_1


Proceed ([y]/n)? y


Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate pelatihan
#
# To deactivate an active environment, use
#
#     $ conda deactivate

(D:\Programs\Programming\Envs\pelatihan) D:\Polban\Penunjang\Pelatihan\pelatihan-ds-swe-code>pip install -r requirements.txt
```

## Menjalankan streamlit pertama kali
```sh
streamlit run abc.py
```

## Git
```sh
echo "# pelatihan-ds-swe-code" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/trisgelar/pelatihan-ds-swe-code.git
git push -u origin main


git remote add origin https://github.com/trisgelar/pelatihan-ds-swe-code.git
git branch -M main
git push -u origin main
```