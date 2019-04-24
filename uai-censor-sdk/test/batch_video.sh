total=100
start=`date +%s`
for ((i=0; i<$total; i++));do
    python create_sync_video_job.py &
    sleep 0.1
done
end=`date +%s`

avg=`echo $start $end $total | awk '{print (($2-$1)*1000/$3)}'`
echo "Average Time: $avg ms"