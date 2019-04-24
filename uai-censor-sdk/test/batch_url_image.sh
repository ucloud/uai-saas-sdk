total=100
start=`date +%s`
for ((i=0; i<$total; i++));do
    for ((j=0; j<100; j++));do
        python create_url_image_job.py &
    done
    sleep 0.1
done

end=`date +%s`
avg=`echo $start $end $total | awk '{print (($2-$1)*1000/$3)}'`
echo "Average: Time: $avg ms"