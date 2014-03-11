db.zips.aggregate( 
[
{
       	$match: {city:{$regex:"^[0-9]"}}
},
{ 
	$group : { _id :  "$city", n : {$sum:1} } 
},
{
	$group : {_id:null, total: {$sum:"$n"}}
}
]
)
