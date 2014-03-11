db.zips.aggregate( { $group :
                         { _id : { state : "$state", city : "$city" },
                           pop : { $sum : "$pop" } } },
                        {$match: {"state":{$in:["CA, NY"]},"pop":{$gt:25000}}},
                       { $group :
                       { _id : "$_id.state",
                         avgCityPop : { $avg : "$pop" } } },
			{$sort : {_id:1}}
)

