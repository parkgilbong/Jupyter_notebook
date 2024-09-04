def Set_WD(base_folder, *args):
    """
    주어진 base folder와 추가 폴더 이름들을 사용하여 경로를 생성하고, 해당 경로를 working directory로 설정합니다. 

    Parameters:
    - base_folder   : 기본 폴더의 절대 경로 
    - *args:        : 추가할 폴더 이름들 (가변인자)

    Example:
        base_folder = 'C:/Users/YGKim_IBS/Documents' 
        Set_WD(base_folder, "test1", "test2")
        =========================================================================
        Directory C:/Users/YGKim_IBS/Documents\test1\test2 created.
        The working directory is set to C:/Users/YGKim_IBS/Documents\test1\test2.
    """

    import os

    #전체 경로 생성
    full_path = os.path.join(base_folder, *args)

    if not os.path.exists(full_path): # If the path does not exist, create the directory 
       os.makedirs(full_path)
       os.chdir(full_path)
       print(f"Directory {full_path} created.")
       print(f"The working directory is set to {full_path}.") 
    else:
         os.chdir(full_path)
         print(f"Directory {full_path} already exists.")
         print(f"The working directory is set to {full_path}.")

################################################################################################################

def Grab_files_in_folder(folder_path, ext=""):
    """
    Return the paths of files with extension *ext* present in *foler*.

    Parameters:
    - folder: 탐색할 폴더의 절대 경로
    - ext: str. 검색할 파일의 확장자. 
    
    Example:
    base = "C:/Users/YGKim_IBS/Documents/Github/Jupyter_notebook/FiberPhotometry"
    Grab_files_in_folder(base, ext='.ipynb')
    """

    import os

    list = []

    for file in os.listdir(folder_path):
        if file.endswith(ext):
            list.append(os.path.join(folder_path, file))

    return(list)

################################################################################################################

def Grab_files_in_all_subfolder(folder_path, ext=""):
    """
    Return the paths of files with extension *ext* present in *all sub-foler*.

    Parameters:
    - folder: 탐색할 root 폴더의 절대 경로
    - ext: str. 검색할 파일의 확장자. 
    
    Example:
    base = "C:/Users/YGKim_IBS/Documents/Github/Jupyter_notebook/FiberPhotometry"
    Grab_files_in_folder(base, ext='.ipynb')
    """

    import os

    list = [os.path.join(root, name) 
            for root, dirs, files in os.walk(folder_path)
            for name in files 
            if name.endswith(ext)]

    return(list)