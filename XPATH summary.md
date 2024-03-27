# XPATH

## sources:

[https://youtu.be/jraDTvKLLvY?si=zZmidqDQcajEgShn](https://youtu.be/jraDTvKLLvY?si=zZmidqDQcajEgShn)

[XPath online real-time tester, evaluator and generator for XML & HTML (xpather.com)](http://xpather.com/XALN8HoB)

```python
//article # return all article in the page
//li/article # / means to look directly to child
#this👆 returns the article that's dirctly inside the list 
# but // finds the elemnt that's somewhere in the parent
//li/article/div[2] # in the second div in every article
//li/article/div[2]/p[1]/@class # @ returns the value of the attribute
//article/div/a/.. # return the parent of the a

//a[@title]/@href #get all elemnt that have title & return thier href
//a[*]  #get all the a that have some element in them not just text
//a[@*] #get all a that have attribute
//div[@class="col-sm-8 h1"]
//div[contains(@class,"col")]

//*[text()] # any elemt contain text
//*[text()[contains(.,"Book")]]
//a[text()[contains(.,"Book")]]

//*[count(.//li)=2] # every elemt that contains 2 li
#select the li taht come after the selected [](https://www.notion.so/Data-since-76e8e3e5f6674ab8879e934375da123e?pvs=21)li
//ul[@class="nav nav-list"]/li/ul/li[1]/following-sibling::*
#slect a div that inside article
//div[ancestor::article]
/text() #returns the text of any elemnt
```

### get name of any book have 1 star

```python
//article/p[contains(@class,"One")]/following-sibling::h3
or
//article[p[contains(@class,"One")]]/h3
# the book name and price using |
//article[p[contains(@class,"One")]]/h3/a | //article[p[contains(@class,"One")]]//p[@class="price_color"]
```

**add_experimental_option  25:40**
