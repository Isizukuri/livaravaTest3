    var title = document.title
    var viewed_requests = []
    var not_viewed_requests = []

    var active_window = Visibility.every(1000, function() {
        document.title = not_viewed_requests.length + " | " + title;
        $.get("/last_requests/", function(data) {
            $('#request_list').empty();
            for (index in data){
                $('#request_list').append($('<li>').append(
                    data[index].timestamp+
                    " url: "+data[index].url+
                    ", method: "+data[index].method
                    )
                );
                if (!viewed_requests.includes(data[index].pk)) {
                    viewed_requests.push(data[index].pk)
                };
            };
        });
    });

    Visibility.change(function (e, state) {
        if (state=='hidden'){
            Visibility.stop(active_window);
            passive_window = setInterval(function(){
                $.get("/last_requests/", function(data) {
                    $('#request_list').empty();
                        for (index in data){
                            $('#request_list').append($('<li>').append(
                                data[index].timestamp+
                                " url: "+data[index].url+
                                ", method: "+data[index].method
                                )
                            );
                        if (!viewed_requests.includes(data[index].pk) && !not_viewed_requests.includes(data[index].pk)) {
                        not_viewed_requests.push(data[index].pk)
                        };
                        };
                    });
                document.title = not_viewed_requests.length + " | " + title;
            }, 1000);
        }
        else if (state=='visible'){
            for (i in not_viewed_requests){
                id = not_viewed_requests[i];
                if (!viewed_requests.includes(id)) {
                    viewed_requests.push(id)
                };
            };
            clearInterval(passive_window)
            not_viewed_requests = []
            document.title = not_viewed_requests.length + " | " + title;
        };
    });
