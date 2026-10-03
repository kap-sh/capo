"""Generated from Smithy shape ``com.amazonaws.elasticache#ServiceUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.boolean_optional
    import capo_elasticache.types.service_update_severity
    import capo_elasticache.types.service_update_status
    import capo_elasticache.types.service_update_type
    import capo_elasticache.types.string
    import capo_elasticache.types.t_stamp


class ServiceUpdate(TypedDict, closed=True):
    service_update_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The unique ID of the service update</p>"""
    service_update_release_date: NotRequired["capo_elasticache.types.t_stamp.TStamp"]
    """<p>The date when the service update is initially available</p>"""
    service_update_end_date: NotRequired["capo_elasticache.types.t_stamp.TStamp"]
    """<p>The date after which the service update is no longer available</p>"""
    service_update_severity: NotRequired[
        "capo_elasticache.types.service_update_severity.ServiceUpdateSeverity"
    ]
    """<p>The severity of the service update</p>"""
    service_update_recommended_apply_by_date: NotRequired[
        "capo_elasticache.types.t_stamp.TStamp"
    ]
    """<p>The recommendend date to apply the service update in order to ensure compliance. For information on compliance, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/elasticache-compliance.html#elasticache-compliance-self-service">Self-Service Security Updates for Compliance</a>.</p>"""
    service_update_status: NotRequired[
        "capo_elasticache.types.service_update_status.ServiceUpdateStatus"
    ]
    """<p>The status of the service update</p>"""
    service_update_description: NotRequired["capo_elasticache.types.string.String"]
    """<p>Provides details of the service update</p>"""
    service_update_type: NotRequired[
        "capo_elasticache.types.service_update_type.ServiceUpdateType"
    ]
    """<p>Reflects the nature of the service update</p>"""
    engine: NotRequired["capo_elasticache.types.string.String"]
    """<p>The Elasticache engine to which the update applies. Either Valkey, Redis OSS or Memcached.</p>"""
    engine_version: NotRequired["capo_elasticache.types.string.String"]
    """<p>The Elasticache engine version to which the update applies. Either Valkey, Redis OSS or Memcached engine version.</p>"""
    auto_update_after_recommended_apply_by_date: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether the service update will be automatically applied once the recommended apply-by date has expired. </p>"""
    estimated_update_time: NotRequired["capo_elasticache.types.string.String"]
    """<p>The estimated length of time the service update will take</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ServiceUpdate, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "service_update_name" in value:
        pairs.append(
            (f"{key_prefix}ServiceUpdateName", str(value["service_update_name"]))
        )
    if "service_update_release_date" in value:
        import capo_elasticache.types.t_stamp

        capo_elasticache.types.t_stamp.serialize_query(
            value["service_update_release_date"],
            pairs,
            f"{key_prefix}ServiceUpdateReleaseDate",
        )
    if "service_update_end_date" in value:
        import capo_elasticache.types.t_stamp

        capo_elasticache.types.t_stamp.serialize_query(
            value["service_update_end_date"], pairs, f"{key_prefix}ServiceUpdateEndDate"
        )
    if "service_update_severity" in value:
        import capo_elasticache.types.service_update_severity

        capo_elasticache.types.service_update_severity.serialize_query(
            value["service_update_severity"],
            pairs,
            f"{key_prefix}ServiceUpdateSeverity",
        )
    if "service_update_recommended_apply_by_date" in value:
        import capo_elasticache.types.t_stamp

        capo_elasticache.types.t_stamp.serialize_query(
            value["service_update_recommended_apply_by_date"],
            pairs,
            f"{key_prefix}ServiceUpdateRecommendedApplyByDate",
        )
    if "service_update_status" in value:
        import capo_elasticache.types.service_update_status

        capo_elasticache.types.service_update_status.serialize_query(
            value["service_update_status"], pairs, f"{key_prefix}ServiceUpdateStatus"
        )
    if "service_update_description" in value:
        pairs.append(
            (
                f"{key_prefix}ServiceUpdateDescription",
                str(value["service_update_description"]),
            )
        )
    if "service_update_type" in value:
        import capo_elasticache.types.service_update_type

        capo_elasticache.types.service_update_type.serialize_query(
            value["service_update_type"], pairs, f"{key_prefix}ServiceUpdateType"
        )
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "auto_update_after_recommended_apply_by_date" in value:
        pairs.append(
            (
                f"{key_prefix}AutoUpdateAfterRecommendedApplyByDate",
                "true"
                if value["auto_update_after_recommended_apply_by_date"]
                else "false",
            )
        )
    if "estimated_update_time" in value:
        pairs.append(
            (f"{key_prefix}EstimatedUpdateTime", str(value["estimated_update_time"]))
        )


def deserialize_query(el: Element) -> ServiceUpdate:
    out: ServiceUpdate = {}  # type: ignore[typeddict-item]
    child_service_update_name = el.find("ServiceUpdateName")
    if child_service_update_name is not None:
        out["service_update_name"] = str(child_service_update_name.text or "")
    child_service_update_release_date = el.find("ServiceUpdateReleaseDate")
    if child_service_update_release_date is not None:
        import capo_elasticache.types.t_stamp

        out["service_update_release_date"] = (
            capo_elasticache.types.t_stamp.deserialize_query(
                child_service_update_release_date
            )
        )
    child_service_update_end_date = el.find("ServiceUpdateEndDate")
    if child_service_update_end_date is not None:
        import capo_elasticache.types.t_stamp

        out["service_update_end_date"] = (
            capo_elasticache.types.t_stamp.deserialize_query(
                child_service_update_end_date
            )
        )
    child_service_update_severity = el.find("ServiceUpdateSeverity")
    if child_service_update_severity is not None:
        import capo_elasticache.types.service_update_severity

        out["service_update_severity"] = (
            capo_elasticache.types.service_update_severity.deserialize_query(
                child_service_update_severity
            )
        )
    child_service_update_recommended_apply_by_date = el.find(
        "ServiceUpdateRecommendedApplyByDate"
    )
    if child_service_update_recommended_apply_by_date is not None:
        import capo_elasticache.types.t_stamp

        out["service_update_recommended_apply_by_date"] = (
            capo_elasticache.types.t_stamp.deserialize_query(
                child_service_update_recommended_apply_by_date
            )
        )
    child_service_update_status = el.find("ServiceUpdateStatus")
    if child_service_update_status is not None:
        import capo_elasticache.types.service_update_status

        out["service_update_status"] = (
            capo_elasticache.types.service_update_status.deserialize_query(
                child_service_update_status
            )
        )
    child_service_update_description = el.find("ServiceUpdateDescription")
    if child_service_update_description is not None:
        out["service_update_description"] = str(
            child_service_update_description.text or ""
        )
    child_service_update_type = el.find("ServiceUpdateType")
    if child_service_update_type is not None:
        import capo_elasticache.types.service_update_type

        out["service_update_type"] = (
            capo_elasticache.types.service_update_type.deserialize_query(
                child_service_update_type
            )
        )
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_auto_update_after_recommended_apply_by_date = el.find(
        "AutoUpdateAfterRecommendedApplyByDate"
    )
    if child_auto_update_after_recommended_apply_by_date is not None:
        out["auto_update_after_recommended_apply_by_date"] = (
            child_auto_update_after_recommended_apply_by_date.text or ""
        ).lower() == "true"
    child_estimated_update_time = el.find("EstimatedUpdateTime")
    if child_estimated_update_time is not None:
        out["estimated_update_time"] = str(child_estimated_update_time.text or "")
    return out
