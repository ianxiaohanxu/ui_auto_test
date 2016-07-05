# File structure

![file_structure](/Users/alexgao/Documents/temp/auto_test_structure.png)



# How to use it

1. On your computer, access your workspace, and then clone the repository

   ```shell
   git clone https://gitlab.uxin001.com:9090/testing/auto_test.git
   ```

   ​

2. Go into the project folder, default name is ```auto_test```, you will see the file structure as the upon image.

   ​

3. Set up virtualenv, refer to [How to set up virtualenv](http://wiki.uxin001.com/pages/viewpage.action?pageId=557197)

   * **Caution 1**: We use ```python2.7```

   * **Caution 2**: Bear in mind, ```activate virtualenv```

   * **Caution 3**: When the ```requirement``` updated, you should upgrade your virtualenv accordingly by ```pip install --upgrade -r requirement/xxx.txt```

     ​

4. Before you run test scripts, you should make a package first

   ```shell
   cd tools
   python package.py sdist
   python package.py install
   ```

   ​

5. Technically, you could run api test scripts now. For UI test scripts, you still need to prepare test device and set up appium server. Whatever, you could run test scripts by: ```robot xxx.robot```. [Learn more about robotframework](http://wiki.uxin001.com/display/uxintest/Automation+test+Books)

   ​

# Git branch strategy

**We have two kind of branches: master branch and _work_ branch. Everybody works on his/her own _work_ branch, after he/she finishes and totally self-test it, make a ```merge request``` to master branch.**

### Git workflow

> ```shell
> # Pull master branch and make a new branch based on it, we prefer the meaningful name (e.g. add_test_cases_for_login, update_test_cases_for_chat_pages).
> git pull origin master:your_branch_name
>
> # Checkout your new branch
> git checkout your_branch_name
>
> # Coding on your branch
> # After you finish and self-test it, rebase on latest master branch. If conflict happens, resolve it and re-test.
> git pull --rebase origin master
>
> # If everything goes well, push your branch onto gitlab. If there is not the branch with the same name on gitlab, you should with -u option.
> git push -u origin your_branch_name
>
> # And then ask a merge request on gitlab, assign it to somebody who will review your code.
> ```

[Learn more about Git](http://wiki.uxin001.com/display/uxintest/Git+Books)