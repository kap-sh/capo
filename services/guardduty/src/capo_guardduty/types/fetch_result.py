"""Generated from Smithy shape ``com.amazonaws.guardduty#FetchResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.count
    import capo_guardduty.types.fetch_detector_features
    import capo_guardduty.types.fetch_item_ids
    import capo_guardduty.types.fetch_verdict
    import capo_guardduty.types.finding_type_documentation


class FetchResult(TypedDict, closed=True):
    item_ids: NotRequired["capo_guardduty.types.fetch_item_ids.FetchItemIds"]
    """<p>The identifiers of the items that were returned, such as finding IDs, event IDs, signal IDs, or account IDs, depending on <code>FetchType</code>. The list contains at most 50 identifiers; <code>TotalCount</code> can be larger.</p>"""
    total_count: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The total number of items that were returned. This value can be greater than the number of identifiers in <code>ItemIds</code>.</p>"""
    features: NotRequired[
        "capo_guardduty.types.fetch_detector_features.FetchDetectorFeatures"
    ]
    """<p>The configuration of the detector features that GuardDuty retrieved.</p>"""
    verdict: NotRequired["capo_guardduty.types.fetch_verdict.FetchVerdict"]
    """<p>The reputation verdict for the threat indicator. Possible values are <code>THREAT</code>, <code>BENIGN</code>, and <code>NEUTRAL</code>. If the lookup returned more than one result, the verdict describes the first result.</p>"""
    documentation: NotRequired[
        "capo_guardduty.types.finding_type_documentation.FindingTypeDocumentation"
    ]
    """<p>The documentation for the finding type that GuardDuty retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FetchResult) -> dict:
    out: dict = {}
    if "item_ids" in value:
        import capo_guardduty.types.fetch_item_ids

        out["itemIds"] = capo_guardduty.types.fetch_item_ids.serialize_json(
            value["item_ids"]
        )
    if "total_count" in value:
        out["totalCount"] = value["total_count"]
    if "features" in value:
        import capo_guardduty.types.fetch_detector_features

        out["features"] = capo_guardduty.types.fetch_detector_features.serialize_json(
            value["features"]
        )
    if "verdict" in value:
        import capo_guardduty.types.fetch_verdict

        out["verdict"] = capo_guardduty.types.fetch_verdict.serialize_json(
            value["verdict"]
        )
    if "documentation" in value:
        import capo_guardduty.types.finding_type_documentation

        out["documentation"] = (
            capo_guardduty.types.finding_type_documentation.serialize_json(
                value["documentation"]
            )
        )
    return out


def deserialize_json(data: dict) -> FetchResult:
    out: FetchResult = {}  # type: ignore[typeddict-item]
    if data.get("itemIds") is not None:
        import capo_guardduty.types.fetch_item_ids

        out["item_ids"] = capo_guardduty.types.fetch_item_ids.deserialize_json(
            data["itemIds"]
        )
    if data.get("totalCount") is not None:
        out["total_count"] = data["totalCount"]
    if data.get("features") is not None:
        import capo_guardduty.types.fetch_detector_features

        out["features"] = capo_guardduty.types.fetch_detector_features.deserialize_json(
            data["features"]
        )
    if data.get("verdict") is not None:
        import capo_guardduty.types.fetch_verdict

        out["verdict"] = capo_guardduty.types.fetch_verdict.deserialize_json(
            data["verdict"]
        )
    if data.get("documentation") is not None:
        import capo_guardduty.types.finding_type_documentation

        out["documentation"] = (
            capo_guardduty.types.finding_type_documentation.deserialize_json(
                data["documentation"]
            )
        )
    return out
