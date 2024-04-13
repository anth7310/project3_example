d3.json("/country_mock", function (data) {
  // Set dimensions and margins for the graph
  const margin = { top: 20, right: 30, bottom: 40, left: 90 },
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

  // Append the SVG object to the div
  const svg = d3
    .select("#my_dataviz1")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  // X axis
  const x = d3
    .scaleLinear()
    .domain([0, Math.max(...data.Value)])
    .range([0, width]);
  svg
    .append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x))
    .selectAll("text")
    .style("text-anchor", "end");

  // Y axis
  const y = d3.scaleBand().range([0, height]).domain(data.Country).padding(0.1);
  svg.append("g").call(d3.axisLeft(y));

  // Bars
  svg
    .selectAll("myRect")
    .data(data.Value)
    .enter()
    .append("rect")
    .attr("x", x(0))
    .attr("y", (d, i) => y(data.Country[i]))
    .attr("width", (d) => x(d))
    .attr("height", y.bandwidth())
    .attr("fill", "#69b3a2");
});
