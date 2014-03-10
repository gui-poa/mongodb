db.zips.aggregate([
{
	 _id: { state: "$state", city: "$city" },
                           popSum: { $sum: "$pop" } 
}
,
{
        $match: {state:"CT",pop:{$gt:25000}}
},
{	
	$group: {_id: "$_id.city",avgCity:{$avg: "$popSum"}}
}
])
