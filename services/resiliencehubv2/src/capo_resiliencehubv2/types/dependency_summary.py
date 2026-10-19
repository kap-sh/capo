"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DependencySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.dependency_criticality
    import capo_resiliencehubv2.types.query_range
    import capo_resiliencehubv2.types.region_list
    import capo_resiliencehubv2.types.uuid


class DependencySummary(TypedDict, closed=True):
    dependency_id: "capo_resiliencehubv2.types.uuid.Uuid"
    """<p>The unique identifier of the dependency.</p>"""
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    dependency_name: "str"
    """<p>The name of the dependency.</p>"""
    dns_name: "str"
    """<p>The DNS name associated with the dependency.</p>"""
    location: "str"
    """<p>The location of the dependency.</p>"""
    last_detected_time: "datetime.datetime"
    """<p>The timestamp when the dependency was last detected.</p>"""
    source_regions: "capo_resiliencehubv2.types.region_list.RegionList"
    """<p>The source Regions from which the dependency was detected.</p>"""
    provider: NotRequired["str"]
    """<p>The provider of the dependency.</p>"""
    query_range: "capo_resiliencehubv2.types.query_range.QueryRange"
    """<p>The query range data for the dependency.</p>"""
    criticality: (
        "capo_resiliencehubv2.types.dependency_criticality.DependencyCriticality"
    )
    """<p>The criticality level of the dependency.</p>"""
    comment: NotRequired["str"]
    """<p>A user-provided comment about the dependency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DependencySummary) -> dict:
    out: dict = {}
    out["dependencyId"] = value["dependency_id"]
    out["serviceArn"] = value["service_arn"]
    out["dependencyName"] = value["dependency_name"]
    out["dnsName"] = value["dns_name"]
    out["location"] = value["location"]
    import capo_resiliencehubv2.types._prelude.timestamp

    out["lastDetectedTime"] = (
        capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["last_detected_time"]
        )
    )
    import capo_resiliencehubv2.types.region_list

    out["sourceRegions"] = capo_resiliencehubv2.types.region_list.serialize_json(
        value["source_regions"]
    )
    if "provider" in value:
        out["provider"] = value["provider"]
    import capo_resiliencehubv2.types.query_range

    out["queryRange"] = capo_resiliencehubv2.types.query_range.serialize_json(
        value["query_range"]
    )
    import capo_resiliencehubv2.types.dependency_criticality

    out["criticality"] = (
        capo_resiliencehubv2.types.dependency_criticality.serialize_json(
            value["criticality"]
        )
    )
    if "comment" in value:
        out["comment"] = value["comment"]
    return out


def deserialize_json(data: dict) -> DependencySummary:
    out: DependencySummary = {}  # type: ignore[typeddict-item]
    if data.get("dependencyId") is not None:
        out["dependency_id"] = data["dependencyId"]
    else:
        out["dependency_id"] = ""
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        out["service_arn"] = ""
    if data.get("dependencyName") is not None:
        out["dependency_name"] = data["dependencyName"]
    else:
        out["dependency_name"] = ""
    if data.get("dnsName") is not None:
        out["dns_name"] = data["dnsName"]
    else:
        out["dns_name"] = ""
    if data.get("location") is not None:
        out["location"] = data["location"]
    else:
        out["location"] = ""
    if data.get("lastDetectedTime") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["last_detected_time"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["lastDetectedTime"]
            )
        )
    else:
        import datetime

        out["last_detected_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("sourceRegions") is not None:
        import capo_resiliencehubv2.types.region_list

        out["source_regions"] = capo_resiliencehubv2.types.region_list.deserialize_json(
            data["sourceRegions"]
        )
    else:
        out["source_regions"] = []
    if data.get("provider") is not None:
        out["provider"] = data["provider"]
    if data.get("queryRange") is not None:
        import capo_resiliencehubv2.types.query_range

        out["query_range"] = capo_resiliencehubv2.types.query_range.deserialize_json(
            data["queryRange"]
        )
    else:
        raise DeserializationError("DependencySummary.query_range required")
    if data.get("criticality") is not None:
        import capo_resiliencehubv2.types.dependency_criticality

        out["criticality"] = (
            capo_resiliencehubv2.types.dependency_criticality.deserialize_json(
                data["criticality"]
            )
        )
    else:
        import typing

        out["criticality"] = typing.cast(
            "capo_resiliencehubv2.types.dependency_criticality.DependencyCriticality",
            "",
        )
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    return out
