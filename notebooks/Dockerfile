FROM jupyter/base-notebook

USER jovyan

# Install Tensorflow
RUN conda install --quiet --yes \    
    'pandas' \
    'pandas-gbq' --channel conda-forge
    