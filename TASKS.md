# TODO Items for YT-CLI

## JSONify Data Map
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



## ContentID Classes
Needed to enbale monetization on videos. 

[API documentation](https://developers.google.com/youtube/partner)

[Full Monetization Example](https://developers.google.com/youtube/partner/upload_claim_sample)

### Demonetization Detection
Behold! The [correct way](https://developers.google.com/youtube/partner/docs/v1/claims#status) to detect video demonetization!

### Monetization Theory
You have to file a `claim` against your own video for 100% of the content on it. You need to set it up so the `claim` is being made by the correct "content owner" being the authenticated account to ensure you get your own monetization. Finally you must apply a `policy` that enables monetization on it.

Think about it like getting other ContentID claims. They claim a portion of the video, set it to be owned by them, and then decided whether or not to monetize that portion. You're essentially following the same procedure to monetize your own video.

