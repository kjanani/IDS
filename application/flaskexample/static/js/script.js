$(document).ready(function () {
		// on page load this will fetch data from our flask-app asynchronously
		$.ajax({url: '/word_cloud', success: function (data) {
				//           // returned data is in string format we have to convert it back into json format
				var words_data = $.parseJSON(data);
				//                         // we will build a word cloud into our div with id=word_cloud
				//                                // we have to specify width and height of the word_cloud chart
				$('#word_cloud').jQCloud(words_data, {
						width: 600,
						height: 600,
						colors: ["#800026", "#bd0026", "#e31a1c", "#fc4e2a", "#fd8d3c", "#feb24c", "#fed976", "#ffeda0", "#ffffcc"],
						fontSize: {
								from: 0.1,
								to: 0.2
						}
				});
		}});
});
