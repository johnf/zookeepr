# Integration Tests

Our integration testing suite uses [lettuce](http://lettuce.it) it is a BDD
suite very similar to [cucumber](http://cuckes.info) from the rails world. We
also hook in [lettuce_webdriver](https://github.com/bbangert/lettuce_webdriver)
for selenium support with chrome and firefox.

At the moment the steps are a bit convoluted and we need a Makefile or script to
make things a bit simpler

## Setting up your environment

If you want to use firefox you will need to install the [Selenium Webdriver
plugin](http://seleniumhq.org/projects/ide/)

For chrome you need to install
[chromdriver](http://code.google.com/p/selenium/downloads/list) and be running
at least chrome >= 12

## Running tests

* Start an instance of Zookeepr with a clean database running on port 6000
* In the Zookeepr sub-directory run **lettuce**
