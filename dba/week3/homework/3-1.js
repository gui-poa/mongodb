db.zips.aggregate(
{
	$group: {_id: "$state", count: {$sum:1}}
},
{
	$sort: {"count":1}
}
)
