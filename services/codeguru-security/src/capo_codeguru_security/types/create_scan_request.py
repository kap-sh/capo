"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#CreateScanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguru_security.types.analysis_type
    import capo_codeguru_security.types.client_token
    import capo_codeguru_security.types.resource_id
    import capo_codeguru_security.types.scan_name
    import capo_codeguru_security.types.scan_type
    import capo_codeguru_security.types.tag_map


class CreateScanRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_codeguru_security.types.client_token.ClientToken"]
    """<p>The idempotency token for the request. Amazon CodeGuru Security uses this value to prevent the accidental creation of duplicate scans if there are failures and retries.</p>"""
    resource_id: "capo_codeguru_security.types.resource_id.ResourceId"
    """<p>The identifier for the resource object to be scanned.</p>"""
    scan_name: "capo_codeguru_security.types.scan_name.ScanName"
    """<p>The unique name that CodeGuru Security uses to track revisions across multiple scans of the same resource. Only allowed for a <code>STANDARD</code> scan type. </p>"""
    scan_type: NotRequired["capo_codeguru_security.types.scan_type.ScanType"]
    """<p>The type of scan, either <code>Standard</code> or <code>Express</code>. Defaults to <code>Standard</code> type if missing.</p> <p> <code>Express</code> scans run on limited resources and use a limited set of detectors to analyze your code in near-real time. <code>Standard</code> scans have standard resource limits and use the full set of detectors to analyze your code.</p>"""
    analysis_type: NotRequired[
        "capo_codeguru_security.types.analysis_type.AnalysisType"
    ]
    """<p>The type of analysis you want CodeGuru Security to perform in the scan, either <code>Security</code> or <code>All</code>. The <code>Security</code> type only generates findings related to security. The <code>All</code> type generates both security findings and quality findings. Defaults to <code>Security</code> type if missing.</p>"""
    tags: NotRequired["capo_codeguru_security.types.tag_map.TagMap"]
    """<p>An array of key-value pairs used to tag a scan. A tag is a custom attribute label with two parts:</p> <ul> <li> <p>A tag key. For example, <code>CostCenter</code>, <code>Environment</code>, or <code>Secret</code>. Tag keys are case sensitive.</p> </li> <li> <p>An optional tag value field. For example, <code>111122223333</code>, <code>Production</code>, or a team name. Omitting the tag value is the same as using an empty string. Tag values are case sensitive.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateScanRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_codeguru_security.types.resource_id

    out["resourceId"] = capo_codeguru_security.types.resource_id.serialize_json(
        value["resource_id"]
    )
    out["scanName"] = value["scan_name"]
    if "scan_type" in value:
        import capo_codeguru_security.types.scan_type

        out["scanType"] = capo_codeguru_security.types.scan_type.serialize_json(
            value["scan_type"]
        )
    if "analysis_type" in value:
        import capo_codeguru_security.types.analysis_type

        out["analysisType"] = capo_codeguru_security.types.analysis_type.serialize_json(
            value["analysis_type"]
        )
    if "tags" in value:
        import capo_codeguru_security.types.tag_map

        out["tags"] = capo_codeguru_security.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateScanRequest:
    out: CreateScanRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("resourceId") is not None:
        import capo_codeguru_security.types.resource_id

        out["resource_id"] = capo_codeguru_security.types.resource_id.deserialize_json(
            data["resourceId"]
        )
    else:
        import capo_codeguru_security.types._unknown

        out["resource_id"] = capo_codeguru_security.types._unknown.UnknownUnionMember(
            ""
        )
    if data.get("scanName") is not None:
        out["scan_name"] = data["scanName"]
    else:
        out["scan_name"] = ""
    if data.get("scanType") is not None:
        import capo_codeguru_security.types.scan_type

        out["scan_type"] = capo_codeguru_security.types.scan_type.deserialize_json(
            data["scanType"]
        )
    if data.get("analysisType") is not None:
        import capo_codeguru_security.types.analysis_type

        out["analysis_type"] = (
            capo_codeguru_security.types.analysis_type.deserialize_json(
                data["analysisType"]
            )
        )
    if data.get("tags") is not None:
        import capo_codeguru_security.types.tag_map

        out["tags"] = capo_codeguru_security.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
