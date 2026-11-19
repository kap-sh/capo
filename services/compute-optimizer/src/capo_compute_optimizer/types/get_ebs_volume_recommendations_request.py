"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetEBSVolumeRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.account_ids
    import capo_compute_optimizer.types.ebs_filters
    import capo_compute_optimizer.types.max_results
    import capo_compute_optimizer.types.next_token
    import capo_compute_optimizer.types.volume_arns


class GetEBSVolumeRecommendationsRequest(TypedDict, closed=True):
    volume_arns: NotRequired["capo_compute_optimizer.types.volume_arns.VolumeArns"]
    """<p>The Amazon Resource Name (ARN) of the volumes for which to return recommendations.</p>"""
    next_token: NotRequired["capo_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to advance to the next page of volume recommendations.</p>"""
    max_results: NotRequired["capo_compute_optimizer.types.max_results.MaxResults"]
    """<p>The maximum number of volume recommendations to return with a single request.</p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>"""
    filters: NotRequired["capo_compute_optimizer.types.ebs_filters.EBSFilters"]
    """<p>An array of objects to specify a filter that returns a more specific list of volume recommendations.</p>"""
    account_ids: NotRequired["capo_compute_optimizer.types.account_ids.AccountIds"]
    """<p>The ID of the Amazon Web Services account for which to return volume recommendations.</p> <p>If your account is the management account of an organization, use this parameter to specify the member account for which you want to return volume recommendations.</p> <p>Only one account ID can be specified per request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEBSVolumeRecommendationsRequest) -> dict:
    out: dict = {}
    if "volume_arns" in value:
        import capo_compute_optimizer.types.volume_arns

        out["volumeArns"] = (
            capo_compute_optimizer.types.volume_arns.serialize_aws_json_1_0(
                value["volume_arns"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filters" in value:
        import capo_compute_optimizer.types.ebs_filters

        out["filters"] = (
            capo_compute_optimizer.types.ebs_filters.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "account_ids" in value:
        import capo_compute_optimizer.types.account_ids

        out["accountIds"] = (
            capo_compute_optimizer.types.account_ids.serialize_aws_json_1_0(
                value["account_ids"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEBSVolumeRecommendationsRequest:
    out: GetEBSVolumeRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("volumeArns") is not None:
        import capo_compute_optimizer.types.volume_arns

        out["volume_arns"] = (
            capo_compute_optimizer.types.volume_arns.deserialize_aws_json_1_0(
                data["volumeArns"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("filters") is not None:
        import capo_compute_optimizer.types.ebs_filters

        out["filters"] = (
            capo_compute_optimizer.types.ebs_filters.deserialize_aws_json_1_0(
                data["filters"]
            )
        )
    if data.get("accountIds") is not None:
        import capo_compute_optimizer.types.account_ids

        out["account_ids"] = (
            capo_compute_optimizer.types.account_ids.deserialize_aws_json_1_0(
                data["accountIds"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetEBSVolumeRecommendationsRequest) -> dict:
    out: dict = {}
    if "volume_arns" in value:
        import capo_compute_optimizer.types.volume_arns

        out["volumeArns"] = capo_compute_optimizer.types.volume_arns.serialize_cbor(
            value["volume_arns"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filters" in value:
        import capo_compute_optimizer.types.ebs_filters

        out["filters"] = capo_compute_optimizer.types.ebs_filters.serialize_cbor(
            value["filters"]
        )
    if "account_ids" in value:
        import capo_compute_optimizer.types.account_ids

        out["accountIds"] = capo_compute_optimizer.types.account_ids.serialize_cbor(
            value["account_ids"]
        )
    return out


def deserialize_cbor(data: dict) -> GetEBSVolumeRecommendationsRequest:
    out: GetEBSVolumeRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("volumeArns") is not None:
        import capo_compute_optimizer.types.volume_arns

        out["volume_arns"] = capo_compute_optimizer.types.volume_arns.deserialize_cbor(
            data["volumeArns"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("filters") is not None:
        import capo_compute_optimizer.types.ebs_filters

        out["filters"] = capo_compute_optimizer.types.ebs_filters.deserialize_cbor(
            data["filters"]
        )
    if data.get("accountIds") is not None:
        import capo_compute_optimizer.types.account_ids

        out["account_ids"] = capo_compute_optimizer.types.account_ids.deserialize_cbor(
            data["accountIds"]
        )
    return out
