psql -U postgres -d ergo << EOF

SELECT users.name, count(d.user_id) AS sum FROM users, (SELECT saves.user_id, sum(exercise_no) FROM saves, courses WHERE saves.course_id=courses.id GROUP BY saves.user_id, saves.course_id) AS d WHERE d.sum > 100 AND d.user_id=users.id GROUP BY users.name order by sum desc;

EOF
