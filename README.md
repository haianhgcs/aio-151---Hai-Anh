# aio-151-Hai-Anh
My study to get familiar with AI/ML/Data Science

# Setup development enviroment
1. Install `virtualenv` package that support to create virtual enviroment (if not install yet):
>pip install virtualenv

2. Create virtual environment named `env`
>py -m venv env

3. Activate the virtual environment
>Set-ExecutionPolicy Unrestricted -Scope Process    # run this command if get error UnauthorizedAccess when activating
>env\Scripts\activate

4. Install packages defined in requirements.txt
>pip install -r requirements.txt

5. Deactivate the virtual environment when finish
>deactivate



# OpenCV version
* opencv-python            #only working with images
* opencv-contrib-python    #support for working videos
* opencv-python-headless   #non-GUI OpenCV

Required Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/