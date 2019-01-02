A web page is composed of HTML components. These HTML components or tags can be ```<head> <body>``` . XML was designed to carry data. HTML has predefined tags while in XML, the user can define their own tag.
HTML Structure:
```
<HTML>
<HEAD>
<TITLE> Title name </TITLE>
... other head elements...
</HEAD>
<BODY>
... document body...
</BODY>
</HTML>
```

XML Structure:
```
<food>
<name>French Toast</name>
<price>$4.50</price>
<description>Thick slices made from our homemade sourdough bread</description>
<calories>600</calories>
</food>
```
Paring is a method of breaking down of structure into its components and parts. This github code parses the both HTML and XML page using Beautiful soup library and extracts the table from it.

The initial part of HTML_XML_Parsing.py code concerntrates on the HTML parsing and later part on the XML parsing. The Table extracted is stored in dataframe and presented. 
