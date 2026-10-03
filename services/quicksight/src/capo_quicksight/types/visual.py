"""Generated from Smithy shape ``com.amazonaws.quicksight#Visual``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.bar_chart_visual
    import capo_quicksight.types.box_plot_visual
    import capo_quicksight.types.combo_chart_visual
    import capo_quicksight.types.custom_content_visual
    import capo_quicksight.types.empty_visual
    import capo_quicksight.types.filled_map_visual
    import capo_quicksight.types.funnel_chart_visual
    import capo_quicksight.types.gauge_chart_visual
    import capo_quicksight.types.geospatial_map_visual
    import capo_quicksight.types.heat_map_visual
    import capo_quicksight.types.histogram_visual
    import capo_quicksight.types.insight_visual
    import capo_quicksight.types.kpi_visual
    import capo_quicksight.types.layer_map_visual
    import capo_quicksight.types.line_chart_visual
    import capo_quicksight.types.pie_chart_visual
    import capo_quicksight.types.pivot_table_visual
    import capo_quicksight.types.plugin_visual
    import capo_quicksight.types.radar_chart_visual
    import capo_quicksight.types.sankey_diagram_visual
    import capo_quicksight.types.scatter_plot_visual
    import capo_quicksight.types.table_visual
    import capo_quicksight.types.tree_map_visual
    import capo_quicksight.types.waterfall_visual
    import capo_quicksight.types.word_cloud_visual


class Visual(TypedDict, closed=True):
    table_visual: NotRequired["capo_quicksight.types.table_visual.TableVisual"]
    """<p>A table visual.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/tabular.html">Using tables as visuals</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    pivot_table_visual: NotRequired[
        "capo_quicksight.types.pivot_table_visual.PivotTableVisual"
    ]
    """<p>A pivot table.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/pivot-table.html">Using pivot tables</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    bar_chart_visual: NotRequired[
        "capo_quicksight.types.bar_chart_visual.BarChartVisual"
    ]
    """<p>A bar chart.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/bar-charts.html">Using bar charts</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    kpi_visual: NotRequired["capo_quicksight.types.kpi_visual.KPIVisual"]
    """<p>A key performance indicator (KPI).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/kpi.html">Using KPIs</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    pie_chart_visual: NotRequired[
        "capo_quicksight.types.pie_chart_visual.PieChartVisual"
    ]
    """<p>A pie or donut chart.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/pie-chart.html">Using pie charts</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    gauge_chart_visual: NotRequired[
        "capo_quicksight.types.gauge_chart_visual.GaugeChartVisual"
    ]
    """<p>A gauge chart.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/gauge-chart.html">Using gauge charts</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    line_chart_visual: NotRequired[
        "capo_quicksight.types.line_chart_visual.LineChartVisual"
    ]
    """<p>A line chart.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/line-charts.html">Using line charts</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    heat_map_visual: NotRequired["capo_quicksight.types.heat_map_visual.HeatMapVisual"]
    """<p>A heat map.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/heat-map.html">Using heat maps</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    tree_map_visual: NotRequired["capo_quicksight.types.tree_map_visual.TreeMapVisual"]
    """<p>A tree map.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/tree-map.html">Using tree maps</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    geospatial_map_visual: NotRequired[
        "capo_quicksight.types.geospatial_map_visual.GeospatialMapVisual"
    ]
    """<p>A geospatial map or a points on map visual.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/point-maps.html">Creating point maps</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    filled_map_visual: NotRequired[
        "capo_quicksight.types.filled_map_visual.FilledMapVisual"
    ]
    """<p>A filled map.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/filled-maps.html">Creating filled maps</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    layer_map_visual: NotRequired[
        "capo_quicksight.types.layer_map_visual.LayerMapVisual"
    ]
    """<p>The properties for a layer map visual</p>"""
    funnel_chart_visual: NotRequired[
        "capo_quicksight.types.funnel_chart_visual.FunnelChartVisual"
    ]
    """<p>A funnel chart.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/funnel-visual-content.html">Using funnel charts</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    scatter_plot_visual: NotRequired[
        "capo_quicksight.types.scatter_plot_visual.ScatterPlotVisual"
    ]
    """<p>A scatter plot.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/scatter-plot.html">Using scatter plots</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    combo_chart_visual: NotRequired[
        "capo_quicksight.types.combo_chart_visual.ComboChartVisual"
    ]
    """<p>A combo chart.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/combo-charts.html">Using combo charts</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    box_plot_visual: NotRequired["capo_quicksight.types.box_plot_visual.BoxPlotVisual"]
    """<p>A box plot.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/box-plots.html">Using box plots</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    waterfall_visual: NotRequired[
        "capo_quicksight.types.waterfall_visual.WaterfallVisual"
    ]
    """<p>A waterfall chart.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/waterfall-chart.html">Using waterfall charts</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    histogram_visual: NotRequired[
        "capo_quicksight.types.histogram_visual.HistogramVisual"
    ]
    """<p>A histogram.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/histogram-charts.html">Using histograms</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    word_cloud_visual: NotRequired[
        "capo_quicksight.types.word_cloud_visual.WordCloudVisual"
    ]
    """<p>A word cloud.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/word-cloud.html">Using word clouds</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    insight_visual: NotRequired["capo_quicksight.types.insight_visual.InsightVisual"]
    """<p>An insight visual.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/computational-insights.html">Working with insights</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    sankey_diagram_visual: NotRequired[
        "capo_quicksight.types.sankey_diagram_visual.SankeyDiagramVisual"
    ]
    """<p>A sankey diagram.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/sankey-diagram.html">Using Sankey diagrams</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    custom_content_visual: NotRequired[
        "capo_quicksight.types.custom_content_visual.CustomContentVisual"
    ]
    """<p>A visual that contains custom content.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/custom-visual-content.html">Using custom visual content</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    empty_visual: NotRequired["capo_quicksight.types.empty_visual.EmptyVisual"]
    """<p>An empty visual.</p>"""
    radar_chart_visual: NotRequired[
        "capo_quicksight.types.radar_chart_visual.RadarChartVisual"
    ]
    """<p>A radar chart visual.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/radar-chart.html">Using radar charts</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    plugin_visual: NotRequired["capo_quicksight.types.plugin_visual.PluginVisual"]
    """<p>The custom plugin visual type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Visual) -> dict:
    out: dict = {}
    if "table_visual" in value:
        import capo_quicksight.types.table_visual

        out["TableVisual"] = capo_quicksight.types.table_visual.serialize_json(
            value["table_visual"]
        )
    if "pivot_table_visual" in value:
        import capo_quicksight.types.pivot_table_visual

        out["PivotTableVisual"] = (
            capo_quicksight.types.pivot_table_visual.serialize_json(
                value["pivot_table_visual"]
            )
        )
    if "bar_chart_visual" in value:
        import capo_quicksight.types.bar_chart_visual

        out["BarChartVisual"] = capo_quicksight.types.bar_chart_visual.serialize_json(
            value["bar_chart_visual"]
        )
    if "kpi_visual" in value:
        import capo_quicksight.types.kpi_visual

        out["KPIVisual"] = capo_quicksight.types.kpi_visual.serialize_json(
            value["kpi_visual"]
        )
    if "pie_chart_visual" in value:
        import capo_quicksight.types.pie_chart_visual

        out["PieChartVisual"] = capo_quicksight.types.pie_chart_visual.serialize_json(
            value["pie_chart_visual"]
        )
    if "gauge_chart_visual" in value:
        import capo_quicksight.types.gauge_chart_visual

        out["GaugeChartVisual"] = (
            capo_quicksight.types.gauge_chart_visual.serialize_json(
                value["gauge_chart_visual"]
            )
        )
    if "line_chart_visual" in value:
        import capo_quicksight.types.line_chart_visual

        out["LineChartVisual"] = capo_quicksight.types.line_chart_visual.serialize_json(
            value["line_chart_visual"]
        )
    if "heat_map_visual" in value:
        import capo_quicksight.types.heat_map_visual

        out["HeatMapVisual"] = capo_quicksight.types.heat_map_visual.serialize_json(
            value["heat_map_visual"]
        )
    if "tree_map_visual" in value:
        import capo_quicksight.types.tree_map_visual

        out["TreeMapVisual"] = capo_quicksight.types.tree_map_visual.serialize_json(
            value["tree_map_visual"]
        )
    if "geospatial_map_visual" in value:
        import capo_quicksight.types.geospatial_map_visual

        out["GeospatialMapVisual"] = (
            capo_quicksight.types.geospatial_map_visual.serialize_json(
                value["geospatial_map_visual"]
            )
        )
    if "filled_map_visual" in value:
        import capo_quicksight.types.filled_map_visual

        out["FilledMapVisual"] = capo_quicksight.types.filled_map_visual.serialize_json(
            value["filled_map_visual"]
        )
    if "layer_map_visual" in value:
        import capo_quicksight.types.layer_map_visual

        out["LayerMapVisual"] = capo_quicksight.types.layer_map_visual.serialize_json(
            value["layer_map_visual"]
        )
    if "funnel_chart_visual" in value:
        import capo_quicksight.types.funnel_chart_visual

        out["FunnelChartVisual"] = (
            capo_quicksight.types.funnel_chart_visual.serialize_json(
                value["funnel_chart_visual"]
            )
        )
    if "scatter_plot_visual" in value:
        import capo_quicksight.types.scatter_plot_visual

        out["ScatterPlotVisual"] = (
            capo_quicksight.types.scatter_plot_visual.serialize_json(
                value["scatter_plot_visual"]
            )
        )
    if "combo_chart_visual" in value:
        import capo_quicksight.types.combo_chart_visual

        out["ComboChartVisual"] = (
            capo_quicksight.types.combo_chart_visual.serialize_json(
                value["combo_chart_visual"]
            )
        )
    if "box_plot_visual" in value:
        import capo_quicksight.types.box_plot_visual

        out["BoxPlotVisual"] = capo_quicksight.types.box_plot_visual.serialize_json(
            value["box_plot_visual"]
        )
    if "waterfall_visual" in value:
        import capo_quicksight.types.waterfall_visual

        out["WaterfallVisual"] = capo_quicksight.types.waterfall_visual.serialize_json(
            value["waterfall_visual"]
        )
    if "histogram_visual" in value:
        import capo_quicksight.types.histogram_visual

        out["HistogramVisual"] = capo_quicksight.types.histogram_visual.serialize_json(
            value["histogram_visual"]
        )
    if "word_cloud_visual" in value:
        import capo_quicksight.types.word_cloud_visual

        out["WordCloudVisual"] = capo_quicksight.types.word_cloud_visual.serialize_json(
            value["word_cloud_visual"]
        )
    if "insight_visual" in value:
        import capo_quicksight.types.insight_visual

        out["InsightVisual"] = capo_quicksight.types.insight_visual.serialize_json(
            value["insight_visual"]
        )
    if "sankey_diagram_visual" in value:
        import capo_quicksight.types.sankey_diagram_visual

        out["SankeyDiagramVisual"] = (
            capo_quicksight.types.sankey_diagram_visual.serialize_json(
                value["sankey_diagram_visual"]
            )
        )
    if "custom_content_visual" in value:
        import capo_quicksight.types.custom_content_visual

        out["CustomContentVisual"] = (
            capo_quicksight.types.custom_content_visual.serialize_json(
                value["custom_content_visual"]
            )
        )
    if "empty_visual" in value:
        import capo_quicksight.types.empty_visual

        out["EmptyVisual"] = capo_quicksight.types.empty_visual.serialize_json(
            value["empty_visual"]
        )
    if "radar_chart_visual" in value:
        import capo_quicksight.types.radar_chart_visual

        out["RadarChartVisual"] = (
            capo_quicksight.types.radar_chart_visual.serialize_json(
                value["radar_chart_visual"]
            )
        )
    if "plugin_visual" in value:
        import capo_quicksight.types.plugin_visual

        out["PluginVisual"] = capo_quicksight.types.plugin_visual.serialize_json(
            value["plugin_visual"]
        )
    return out


def deserialize_json(data: dict) -> Visual:
    out: Visual = {}  # type: ignore[typeddict-item]
    if data.get("TableVisual") is not None:
        import capo_quicksight.types.table_visual

        out["table_visual"] = capo_quicksight.types.table_visual.deserialize_json(
            data["TableVisual"]
        )
    if data.get("PivotTableVisual") is not None:
        import capo_quicksight.types.pivot_table_visual

        out["pivot_table_visual"] = (
            capo_quicksight.types.pivot_table_visual.deserialize_json(
                data["PivotTableVisual"]
            )
        )
    if data.get("BarChartVisual") is not None:
        import capo_quicksight.types.bar_chart_visual

        out["bar_chart_visual"] = (
            capo_quicksight.types.bar_chart_visual.deserialize_json(
                data["BarChartVisual"]
            )
        )
    if data.get("KPIVisual") is not None:
        import capo_quicksight.types.kpi_visual

        out["kpi_visual"] = capo_quicksight.types.kpi_visual.deserialize_json(
            data["KPIVisual"]
        )
    if data.get("PieChartVisual") is not None:
        import capo_quicksight.types.pie_chart_visual

        out["pie_chart_visual"] = (
            capo_quicksight.types.pie_chart_visual.deserialize_json(
                data["PieChartVisual"]
            )
        )
    if data.get("GaugeChartVisual") is not None:
        import capo_quicksight.types.gauge_chart_visual

        out["gauge_chart_visual"] = (
            capo_quicksight.types.gauge_chart_visual.deserialize_json(
                data["GaugeChartVisual"]
            )
        )
    if data.get("LineChartVisual") is not None:
        import capo_quicksight.types.line_chart_visual

        out["line_chart_visual"] = (
            capo_quicksight.types.line_chart_visual.deserialize_json(
                data["LineChartVisual"]
            )
        )
    if data.get("HeatMapVisual") is not None:
        import capo_quicksight.types.heat_map_visual

        out["heat_map_visual"] = capo_quicksight.types.heat_map_visual.deserialize_json(
            data["HeatMapVisual"]
        )
    if data.get("TreeMapVisual") is not None:
        import capo_quicksight.types.tree_map_visual

        out["tree_map_visual"] = capo_quicksight.types.tree_map_visual.deserialize_json(
            data["TreeMapVisual"]
        )
    if data.get("GeospatialMapVisual") is not None:
        import capo_quicksight.types.geospatial_map_visual

        out["geospatial_map_visual"] = (
            capo_quicksight.types.geospatial_map_visual.deserialize_json(
                data["GeospatialMapVisual"]
            )
        )
    if data.get("FilledMapVisual") is not None:
        import capo_quicksight.types.filled_map_visual

        out["filled_map_visual"] = (
            capo_quicksight.types.filled_map_visual.deserialize_json(
                data["FilledMapVisual"]
            )
        )
    if data.get("LayerMapVisual") is not None:
        import capo_quicksight.types.layer_map_visual

        out["layer_map_visual"] = (
            capo_quicksight.types.layer_map_visual.deserialize_json(
                data["LayerMapVisual"]
            )
        )
    if data.get("FunnelChartVisual") is not None:
        import capo_quicksight.types.funnel_chart_visual

        out["funnel_chart_visual"] = (
            capo_quicksight.types.funnel_chart_visual.deserialize_json(
                data["FunnelChartVisual"]
            )
        )
    if data.get("ScatterPlotVisual") is not None:
        import capo_quicksight.types.scatter_plot_visual

        out["scatter_plot_visual"] = (
            capo_quicksight.types.scatter_plot_visual.deserialize_json(
                data["ScatterPlotVisual"]
            )
        )
    if data.get("ComboChartVisual") is not None:
        import capo_quicksight.types.combo_chart_visual

        out["combo_chart_visual"] = (
            capo_quicksight.types.combo_chart_visual.deserialize_json(
                data["ComboChartVisual"]
            )
        )
    if data.get("BoxPlotVisual") is not None:
        import capo_quicksight.types.box_plot_visual

        out["box_plot_visual"] = capo_quicksight.types.box_plot_visual.deserialize_json(
            data["BoxPlotVisual"]
        )
    if data.get("WaterfallVisual") is not None:
        import capo_quicksight.types.waterfall_visual

        out["waterfall_visual"] = (
            capo_quicksight.types.waterfall_visual.deserialize_json(
                data["WaterfallVisual"]
            )
        )
    if data.get("HistogramVisual") is not None:
        import capo_quicksight.types.histogram_visual

        out["histogram_visual"] = (
            capo_quicksight.types.histogram_visual.deserialize_json(
                data["HistogramVisual"]
            )
        )
    if data.get("WordCloudVisual") is not None:
        import capo_quicksight.types.word_cloud_visual

        out["word_cloud_visual"] = (
            capo_quicksight.types.word_cloud_visual.deserialize_json(
                data["WordCloudVisual"]
            )
        )
    if data.get("InsightVisual") is not None:
        import capo_quicksight.types.insight_visual

        out["insight_visual"] = capo_quicksight.types.insight_visual.deserialize_json(
            data["InsightVisual"]
        )
    if data.get("SankeyDiagramVisual") is not None:
        import capo_quicksight.types.sankey_diagram_visual

        out["sankey_diagram_visual"] = (
            capo_quicksight.types.sankey_diagram_visual.deserialize_json(
                data["SankeyDiagramVisual"]
            )
        )
    if data.get("CustomContentVisual") is not None:
        import capo_quicksight.types.custom_content_visual

        out["custom_content_visual"] = (
            capo_quicksight.types.custom_content_visual.deserialize_json(
                data["CustomContentVisual"]
            )
        )
    if data.get("EmptyVisual") is not None:
        import capo_quicksight.types.empty_visual

        out["empty_visual"] = capo_quicksight.types.empty_visual.deserialize_json(
            data["EmptyVisual"]
        )
    if data.get("RadarChartVisual") is not None:
        import capo_quicksight.types.radar_chart_visual

        out["radar_chart_visual"] = (
            capo_quicksight.types.radar_chart_visual.deserialize_json(
                data["RadarChartVisual"]
            )
        )
    if data.get("PluginVisual") is not None:
        import capo_quicksight.types.plugin_visual

        out["plugin_visual"] = capo_quicksight.types.plugin_visual.deserialize_json(
            data["PluginVisual"]
        )
    return out
