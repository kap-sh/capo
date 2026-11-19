"""Generated from Smithy shape ``com.amazonaws.cloudwatch#GetOTelEnrichmentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.o_tel_enrichment_metric_selector_list
    import capo_cloudwatch.types.o_tel_enrichment_status
    import capo_cloudwatch.types.timestamp


class GetOTelEnrichmentOutput(TypedDict, closed=True):
    status: NotRequired[
        "capo_cloudwatch.types.o_tel_enrichment_status.OTelEnrichmentStatus"
    ]
    """<p>The status of OTel enrichment for the account. Valid values are <code>Running</code> (enrichment is enabled) and <code>Stopped</code> (enrichment is disabled).</p>"""
    include_filters: NotRequired[
        "capo_cloudwatch.types.o_tel_enrichment_metric_selector_list.OTelEnrichmentMetricSelectorList"
    ]
    """<p>The metric namespaces, and the metric names, that are enriched. This parameter is omitted when enrichment is stopped, and when enrichment is running with no include filters, which means that every supported namespace is in scope.</p>"""
    exclude_filters: NotRequired[
        "capo_cloudwatch.types.o_tel_enrichment_metric_selector_list.OTelEnrichmentMetricSelectorList"
    ]
    """<p>The metric namespaces, and the metric names, that are left unenriched. This parameter is omitted when enrichment is stopped, and when enrichment is running with no exclude filters, which means that nothing is excluded.</p>"""
    created_at: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The date and time that enrichment started for the account. This parameter is omitted when enrichment is stopped.</p>"""
    updated_at: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The date and time that the enrichment configuration for the account was last stored.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetOTelEnrichmentOutput) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_cloudwatch.types.o_tel_enrichment_status

        out["Status"] = (
            capo_cloudwatch.types.o_tel_enrichment_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
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
    if "created_at" in value:
        import capo_cloudwatch.types.timestamp

        out["CreatedAt"] = capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_cloudwatch.types.timestamp

        out["UpdatedAt"] = capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["updated_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetOTelEnrichmentOutput:
    out: GetOTelEnrichmentOutput = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_cloudwatch.types.o_tel_enrichment_status

        out["status"] = (
            capo_cloudwatch.types.o_tel_enrichment_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
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
    if data.get("CreatedAt") is not None:
        import capo_cloudwatch.types.timestamp

        out["created_at"] = capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_cloudwatch.types.timestamp

        out["updated_at"] = capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["UpdatedAt"]
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: GetOTelEnrichmentOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "status" in value:
        import capo_cloudwatch.types.o_tel_enrichment_status

        capo_cloudwatch.types.o_tel_enrichment_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
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
    if "created_at" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["created_at"], pairs, f"{key_prefix}CreatedAt"
        )
    if "updated_at" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["updated_at"], pairs, f"{key_prefix}UpdatedAt"
        )


def deserialize_query(el: Element) -> GetOTelEnrichmentOutput:
    out: GetOTelEnrichmentOutput = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudwatch.types.o_tel_enrichment_status

        out["status"] = capo_cloudwatch.types.o_tel_enrichment_status.deserialize_query(
            child_status
        )
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
    child_created_at = el.find("CreatedAt")
    if child_created_at is not None:
        import capo_cloudwatch.types.timestamp

        out["created_at"] = capo_cloudwatch.types.timestamp.deserialize_query(
            child_created_at
        )
    child_updated_at = el.find("UpdatedAt")
    if child_updated_at is not None:
        import capo_cloudwatch.types.timestamp

        out["updated_at"] = capo_cloudwatch.types.timestamp.deserialize_query(
            child_updated_at
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetOTelEnrichmentOutput) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_cloudwatch.types.o_tel_enrichment_status

        out["Status"] = capo_cloudwatch.types.o_tel_enrichment_status.serialize_cbor(
            value["status"]
        )
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
    if "created_at" in value:
        import capo_cloudwatch.types.timestamp

        out["CreatedAt"] = capo_cloudwatch.types.timestamp.serialize_cbor(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_cloudwatch.types.timestamp

        out["UpdatedAt"] = capo_cloudwatch.types.timestamp.serialize_cbor(
            value["updated_at"]
        )
    return out


def deserialize_cbor(data: dict) -> GetOTelEnrichmentOutput:
    out: GetOTelEnrichmentOutput = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_cloudwatch.types.o_tel_enrichment_status

        out["status"] = capo_cloudwatch.types.o_tel_enrichment_status.deserialize_cbor(
            data["Status"]
        )
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
    if data.get("CreatedAt") is not None:
        import capo_cloudwatch.types.timestamp

        out["created_at"] = capo_cloudwatch.types.timestamp.deserialize_cbor(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_cloudwatch.types.timestamp

        out["updated_at"] = capo_cloudwatch.types.timestamp.deserialize_cbor(
            data["UpdatedAt"]
        )
    return out
