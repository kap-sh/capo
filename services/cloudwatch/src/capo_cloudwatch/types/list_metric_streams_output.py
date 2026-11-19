"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ListMetricStreamsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.metric_stream_entries
    import capo_cloudwatch.types.next_token


class ListMetricStreamsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_cloudwatch.types.next_token.NextToken"]
    """<p>The token that marks the start of the next batch of returned results. You can use this token in a subsequent operation to get the next batch of results.</p>"""
    entries: NotRequired[
        "capo_cloudwatch.types.metric_stream_entries.MetricStreamEntries"
    ]
    """<p>The array of metric stream information.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListMetricStreamsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "entries" in value:
        import capo_cloudwatch.types.metric_stream_entries

        out["Entries"] = (
            capo_cloudwatch.types.metric_stream_entries.serialize_aws_json_1_0(
                value["entries"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListMetricStreamsOutput:
    out: ListMetricStreamsOutput = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Entries") is not None:
        import capo_cloudwatch.types.metric_stream_entries

        out["entries"] = (
            capo_cloudwatch.types.metric_stream_entries.deserialize_aws_json_1_0(
                data["Entries"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ListMetricStreamsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "entries" in value:
        import capo_cloudwatch.types.metric_stream_entries

        capo_cloudwatch.types.metric_stream_entries.serialize_query(
            value["entries"], pairs, f"{key_prefix}Entries"
        )


def deserialize_query(el: Element) -> ListMetricStreamsOutput:
    out: ListMetricStreamsOutput = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_entries = el.find("Entries")
    if child_entries is not None:
        import capo_cloudwatch.types.metric_stream_entries

        out["entries"] = capo_cloudwatch.types.metric_stream_entries.deserialize_query(
            child_entries
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListMetricStreamsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "entries" in value:
        import capo_cloudwatch.types.metric_stream_entries

        out["Entries"] = capo_cloudwatch.types.metric_stream_entries.serialize_cbor(
            value["entries"]
        )
    return out


def deserialize_cbor(data: dict) -> ListMetricStreamsOutput:
    out: ListMetricStreamsOutput = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Entries") is not None:
        import capo_cloudwatch.types.metric_stream_entries

        out["entries"] = capo_cloudwatch.types.metric_stream_entries.deserialize_cbor(
            data["Entries"]
        )
    return out
