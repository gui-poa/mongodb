db.grades.aggregate(
{
        $unwind: "$scores"
},
{
	$match: {"scores.type": {$in: ["homework","exam"]}}
},
{
	$group: {_id: {student_id:"$student_id",class_id:"$class_id"}, avgStudent: {$avg: "$scores.score"}}
},
{
	$group: {_id: "$_id.class_id",avgClass: {$avg:"$avgStudent"}}
},
{
	$sort: {avgClass: 1}
}
)

