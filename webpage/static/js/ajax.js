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
				console.log(e);
				$("#leaderboard").append("<li>"+e[0]+": "+e[1]+"</li>");
			});
		},
		complete: function()
		{
			setTimeout(update, INTERVAL);
		}
	});
}

