"""Generated from Smithy shape ``com.amazonaws.cloudwatch#UpdateOTelEnrichmentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.o_tel_enrichment_metric_selector_list


class UpdateOTelEnrichmentInput(TypedDict, closed=True):
    include_filters: NotRequired[
        "capo_cloudwatch.types.o_tel_enrichment_metric_selector_list.OTelEnrichmentMetricSelectorList"
    ]
    """<p>The metric namespaces, and the metric names, to enrich. If this parameter is omitted, every namespace that Amazon CloudWatch supports for enrichment is in scope.</p> <p>A maximum of 100 filters is allowed across <code>IncludeFilters</code> and <code>ExcludeFilters</code> combined.</p>"""
    exclude_filters: NotRequired[
        "capo_cloudwatch.types.o_tel_enrichment_metric_selector_list.OTelEnrichmentMetricSelectorList"
    ]
    """<p>The metric namespaces, and the metric names, to leave unenriched. If this parameter is omitted, nothing is excluded.</p> <p>Amazon CloudWatch applies <code>ExcludeFilters</code> after <code>IncludeFilters</code>, so a metric that both parameters match is not enriched.</p> <p>A maximum of 100 filters is allowed across <code>IncludeFilters</code> and <code>ExcludeFilters</code> combined.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateOTelEnrichmentInput) -> dict:
    out: dict = {}
    if "include_filters" in value:
        import capo_cloudwatch.types.o_tel_enrichment_metric_selector_list

        out["IncludeFilters"] = (
            capo_cloudwatch.types.o_tel_enrichment_metric_selector_list.serialize_aws_json_1_0(
                value["include_filters"]
            )
        )
    if "exclude_filters" in value:
        import capo_cloudwatch.types.o_tel_enrichment_metric_selector_list

        out["ExcludeFilters"] = (
            capo_cloudwatch.types.o_tel_enrichment_metric_selector_list.serialize_aws_json_1_0(
                value["exclude_filters"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateOTelEnrichmentInput:
    out: UpdateOTelEnrichmentInput = {}  # type: ignore[typeddict-item]
    if data.get("IncludeFilters") is not None:
        import capo_cloudwatch.types.o_tel_enrichment_metric_selector_list

        out["include_filters"] = (
            capo_cloudwatch.types.o_tel_enrichment_metric_selector_list.deserialize_aws_json_1_0(
                data["IncludeFilters"]
            )
        )
    if data.get("ExcludeFilters") is not None:
        import capo_cloudwatch.types.o_tel_enrichment_metric_selector_list

        out["exclude_filters"] = (
            capo_cloudwatch.types.o_tel_enrichment_metric_selector_list.deserialize_aws_json_1_0(
                data["ExcludeFilters"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateOTelEnrichmentInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "include_filters" in value:
        import capo_cloudwatch.types.o_tel_enrichment_metric_selector_list

        capo_cloudwatch.types.o_tel_enrichment_metric_selector_list.serialize_query(
            value["include_filters"], pairs, f"{key_prefix}IncludeFilters"
        )
    if "exclude_filters" in value:
        import capo_cloudwatch.types.o_tel_enrichment_metric_selector_list

        capo_cloudwatch.types.o_tel_enrichment_metric_selector_list.serialize_query(
            value["exclude_filters"], pairs, f"{key_prefix}ExcludeFilters"
        )


def deserialize_query(el: Element) -> UpdateOTelEnrichmentInput:
    out: UpdateOTelEnrichmentInput = {}  # type: ignore[typeddict-item]
    child_include_filters = el.find("IncludeFilters")
    if child_include_filters is not None:
        import capo_cloudwatch.types.o_tel_enrichment_metric_selector_list

        out["include_filters"] = (
            capo_cloudwatch.types.o_tel_enrichment_metric_selector_list.deserialize_query(
                child_include_filters
            )
        )
    child_exclude_filters = el.find("ExcludeFilters")
    if child_exclude_filters is not None:
        import capo_cloudwatch.types.o_tel_enrichment_metric_selector_list

        out["exclude_filters"] = (
            capo_cloudwatch.types.o_tel_enrichment_metric_selector_list.deserialize_query(
                child_exclude_filters
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateOTelEnrichmentInput) -> dict:
    out: dict = {}
    if "include_filters" in value:
        import capo_cloudwatch.types.o_tel_enrichment_metric_selector_list

        out["IncludeFilters"] = (
            capo_cloudwatch.types.o_tel_enrichment_metric_selector_list.serialize_cbor(
                value["include_filters"]
            )
        )
    if "exclude_filters" in value:
        import capo_cloudwatch.types.o_tel_enrichment_metric_selector_list

        out["ExcludeFilters"] = (
            capo_cloudwatch.types.o_tel_enrichment_metric_selector_list.serialize_cbor(
                value["exclude_filters"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UpdateOTelEnrichmentInput:
    out: UpdateOTelEnrichmentInput = {}  # type: ignore[typeddict-item]
    if data.get("IncludeFilters") is not None:
        import capo_cloudwatch.types.o_tel_enrichment_metric_selector_list

        out["include_filters"] = (
            capo_cloudwatch.types.o_tel_enrichment_metric_selector_list.deserialize_cbor(
                data["IncludeFilters"]
            )
        )
    if data.get("ExcludeFilters") is not None:
        import capo_cloudwatch.types.o_tel_enrichment_metric_selector_list

        out["exclude_filters"] = (
            capo_cloudwatch.types.o_tel_enrichment_metric_selector_list.deserialize_cbor(
                data["ExcludeFilters"]
            )
        )
    return out
