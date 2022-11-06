/* Polling interval for updates. */
const INTERVAL = 1000;

/* Begin periodic AJAX updates after the document is ready. */
$(document).ready(function()
{
	update();
});

/* Update the application using AJAX by sending a query. */
function update()
{
	$.ajax(
	{
		url: "/ajax/update",
		type: "GET",
		dataType: "json",
		success: function(response)
		{
			$("#leaderboard").empty();
			response["Leaderboard"].forEach(function (e)
			{
				$("#leaderboard").append("<li>"+e[0]+": "+e[1]+"</li>");
			});

			$("#pwns-table").empty();
			$("#pwns-table").append("<tr><th>Found by</th><th>Username</th><th>Password</th><th>Website</th></tr>");
			response["pwns"].forEach(function (e)
			{
				$("#pwns-table").append("<tr><td>"+e[0]+"</td><td>"+e[1]+"</td><td>"+e[2]+"</td><td>"+e[3]+"</td></li>");
			});
		},
		complete: function()
		{
			setTimeout(update, INTERVAL);
		}
	});
}

