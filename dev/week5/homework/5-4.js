db.zips.aggregate(
{
	$match: {city:{$regex:"^[0-9]"}}
},
{
	$group: { _id: "$_id",sumPop:{$sum:"$pop"}}
},
{
	$group: {_id:null,total:{$sum:"$sumPop"}}
}
)
