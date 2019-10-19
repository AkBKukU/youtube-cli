# TODO Items for YT-CLI

## Major

Larger scale projects

### JSONify Data Map
Allow loading data from differently formatted sources by providing a list of 
tuples for mapping for class fields. Writing to different formats is not 
currently an object but may be done in the future. For now assume that classes
will be saved with `json.dump()`.

Data maps should be a list of attribute name pairs, `{["to","from"]}`. It should
be possible to load different data maps for different sources in the same 
object.

This feature should be optional and data maps will be supplied in the 
`json_read` method call. If it is not supplied it should fall back to 
assuming the same data structure as the class itself that can be dynamically 
loaded. The current functionality of `json_read` should be moved to a new 
method `json_read_all` and the data map code should be put in a new method
`json_read_map`. The correct method will be called based on `if data_map==None`.





