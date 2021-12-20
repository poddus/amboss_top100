# About
This is just a quick and dirty script to create Amboss top100 test sessions. It uses the selenium web driver which in this case is implemented for Firefox.

[Amboss](https://www.amboss.com/de/) is a platform which (among other things) helps medical students prepare for their medical licensing exams.
By (only) practicing the 100 Topics that occur most often in the exam, it is possible to greatly increase learning efficiency (and know more about the things you actually see regularly in practice)
While this is not a native function of the platform, practice sessions can be created manually by selecting topics.
This script bridges the gap by automating the process.

# Instructions
1. get Firefox  
https://www.mozilla.org/en-US/firefox/new/
2. install Selenium WebDriver for Firefox  
https://github.com/mozilla/geckodriver
3. install Python language bindings for Selenium WebDriver  
`pip install selenium`
4. input Amboss username and password into script
5. run script using  
`python ./top100.py`
