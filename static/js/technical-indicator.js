$(document).ready(function() {
    $("#sector").select2({
        width: "100%"
    });
    $("#indicator").select2({
        width: "100%"
    });
    $("#criteria").select2({
        width: "100%"
    });
    $("#techIndicator").DataTable({
        lengthMenu: [10, 25, 50, 100]
    });
});

$(document)
    .on(
        "change",
        "#indicator",
        function() {
            var indic = $("#indicator").val();
            if (indic == "EMA") {
                $("#criteria")
                    .html(
                        '<option value="">--- Choose Criteria ---</option>' +
                        '<option value="GOLDEN">Golden Crossover</option>' +
                        '<option value="DEAD">Dead Crossover</option>' +
                        '<option value="LTPBEMA5">LTP < 5 Days EMA</option>' +
                        '<option value="LTPAEMA5">LTP > 5 Days EMA</option>' +
                        '<option value="LTPBEMA20">LTP < 20 Days EMA</option>' +
                        '<option value="LTPAEMA20">LTP > 20 Days EMA</option>' +
                        '<option value="LTPBEMA45">LTP < 45 Days EMA</option>' +
                        '<option value="LTPAEMA45">LTP > 45 Days EMA</option>' +
                        '<option value="LTPBEMA180">LTP < 180 Days EMA</option>' +
                        '<option value="LTPAEMA180">LTP > 180 Days EMA</option>');
            } else if (indic == "RSI") {
                $("#criteria")
                    .html(
                        '<option value="">--- Choose Criteria ---</option>' +
                        '<option value="RSIB30">RSI < 30</option>' +
                        '<option value="RSIA70">RSI > 70</option>');
            } else if (indic == "MACD") {
                $("#criteria")
                    .html(
                        '<option value="">--- Choose Criteria ---</option>' +
                        '<option value="MACDB0">MACD < 0</option>' +
                        '<option value="MACDA0">MACD > 0</option>');
            } else if (indic == "SMA") {
                $("#criteria")
                    .html(
                        '<option value="">--- Choose Criteria ---</option>' +
                        '<option value="LTPBSMA5">LTP < 5 Days SMA</option>' +
                        '<option value="LTPASMA5">LTP > 5 Days SMA</option>' +
                        '<option value="LTPBSMA20">LTP < 20 Days SMA</option>' +
                        '<option value="LTPASMA20">LTP > 20 Days SMA</option>' +
                        '<option value="LTPBSMA45">LTP < 45 Days SMA</option>' +
                        '<option value="LTPASMA45">LTP > 45 Days SMA</option>' +
                        '<option value="LTPBSMA180">LTP < 180 Days SMA</option>' +
                        '<option value="LTPASMA180">LTP > 180 Days SMA</option>');
            } else {
                $("#criteria")
                    .html(
                        '<option value="">--- Choose Criteria ---</option>');
            }

        });

$(document)
    .on(
        "click",
        "#clickMeId",
        function() {
            var sector = $("#sector").val();
            var indicator = $("#indicator").val();
            var criteria = $("#criteria").val();
            if (sector == "" || indicator == "" || criteria == "") {
                alert("Please enter valid data/s.");
            } else {
                $(".tableWrapper").html($("#loaderImage").html());
                $(".tableWrapper").css("text-align", "center");
                var url = $("#technicalDashboardUrl").text();
                $
                    .ajax({
                        url: url,
                        type: "GET",
                        data: {
                            sector: sector,
                            indicator: indicator,
                            criteria: criteria
                        },
                        success: function(result) {
                            $(".tableWrapper").removeAttr("style");
                            $(".tableWrapper").html(result);
                            $("#techIndicator").DataTable({
                                lengthMenu: [10, 25, 50, 100]
                            });
                        },
                        error: function(xhr, textStatus,
                            errorThrown) {
                            if (xhr.status == 403 ||
                                textStatus == 'parsererror' &&
                                xhr.responseText
                                .match('rememberMe').length > 0) {
                                location.reload();
                            }
                            $(".tableWrapper").removeAttr("style");
                            $(".tableWrapper").html("");
                        }
                    });
            }
        });