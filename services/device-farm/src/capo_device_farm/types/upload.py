"""Generated from Smithy shape ``com.amazonaws.devicefarm#Upload``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name
    import capo_device_farm.types.content_type
    import capo_device_farm.types.date_time
    import capo_device_farm.types.message
    import capo_device_farm.types.metadata
    import capo_device_farm.types.name
    import capo_device_farm.types.sensitive_url
    import capo_device_farm.types.upload_category
    import capo_device_farm.types.upload_status
    import capo_device_farm.types.upload_type


class Upload(TypedDict, closed=True):
    arn: NotRequired["capo_device_farm.types.amazon_resource_name.AmazonResourceName"]
    """<p>The upload's ARN.</p>"""
    name: NotRequired["capo_device_farm.types.name.Name"]
    """<p>The upload's file name.</p>"""
    created: NotRequired["capo_device_farm.types.date_time.DateTime"]
    """<p>When the upload was created.</p>"""
    type: NotRequired["capo_device_farm.types.upload_type.UploadType"]
    """<p>The upload's type.</p> <p>Must be one of the following values:</p> <ul> <li> <p>ANDROID_APP</p> </li> <li> <p>IOS_APP</p> </li> <li> <p>WEB_APP</p> </li> <li> <p>EXTERNAL_DATA</p> </li> <li> <p>APPIUM_JAVA_JUNIT_TEST_PACKAGE</p> </li> <li> <p>APPIUM_JAVA_TESTNG_TEST_PACKAGE</p> </li> <li> <p>APPIUM_PYTHON_TEST_PACKAGE</p> </li> <li> <p>APPIUM_NODE_TEST_PACKAGE</p> </li> <li> <p>APPIUM_RUBY_TEST_PACKAGE</p> </li> <li> <p>APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE</p> </li> <li> <p>APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE</p> </li> <li> <p>APPIUM_WEB_PYTHON_TEST_PACKAGE</p> </li> <li> <p>APPIUM_WEB_NODE_TEST_PACKAGE</p> </li> <li> <p>APPIUM_WEB_RUBY_TEST_PACKAGE</p> </li> <li> <p>INSTRUMENTATION_TEST_PACKAGE</p> </li> <li> <p>XCTEST_TEST_PACKAGE</p> </li> <li> <p>XCTEST_UI_TEST_PACKAGE</p> </li> <li> <p>APPIUM_JAVA_JUNIT_TEST_SPEC</p> </li> <li> <p>APPIUM_JAVA_TESTNG_TEST_SPEC</p> </li> <li> <p>APPIUM_PYTHON_TEST_SPEC</p> </li> <li> <p>APPIUM_NODE_TEST_SPEC</p> </li> <li> <p>APPIUM_RUBY_TEST_SPEC</p> </li> <li> <p>APPIUM_WEB_JAVA_JUNIT_TEST_SPEC</p> </li> <li> <p>APPIUM_WEB_JAVA_TESTNG_TEST_SPEC</p> </li> <li> <p>APPIUM_WEB_PYTHON_TEST_SPEC</p> </li> <li> <p>APPIUM_WEB_NODE_TEST_SPEC</p> </li> <li> <p>APPIUM_WEB_RUBY_TEST_SPEC</p> </li> <li> <p>INSTRUMENTATION_TEST_SPEC</p> </li> <li> <p>XCTEST_UI_TEST_SPEC</p> </li> </ul>"""
    status: NotRequired["capo_device_farm.types.upload_status.UploadStatus"]
    """<p>The upload's status.</p> <p>Must be one of the following values:</p> <ul> <li> <p>FAILED</p> </li> <li> <p>INITIALIZED</p> </li> <li> <p>PROCESSING</p> </li> <li> <p>SUCCEEDED</p> </li> </ul>"""
    url: NotRequired["capo_device_farm.types.sensitive_url.SensitiveURL"]
    """<p>The presigned Amazon S3 URL that was used to store a file using a PUT request.</p>"""
    metadata: NotRequired["capo_device_farm.types.metadata.Metadata"]
    """<p>The upload's metadata. For example, for Android, this contains information that is parsed from the manifest and is displayed in the AWS Device Farm console after the associated app is uploaded.</p>"""
    content_type: NotRequired["capo_device_farm.types.content_type.ContentType"]
    """<p>The upload's content type (for example, <code>application/octet-stream</code>).</p>"""
    message: NotRequired["capo_device_farm.types.message.Message"]
    """<p>A message about the upload's result.</p>"""
    category: NotRequired["capo_device_farm.types.upload_category.UploadCategory"]
    """<p>The upload's category. Allowed values include:</p> <ul> <li> <p>CURATED: An upload managed by AWS Device Farm.</p> </li> <li> <p>PRIVATE: An upload managed by the AWS Device Farm customer.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Upload) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "created" in value:
        import capo_device_farm.types.date_time

        out["created"] = capo_device_farm.types.date_time.serialize_aws_json_1_1(
            value["created"]
        )
    if "type" in value:
        import capo_device_farm.types.upload_type

        out["type"] = capo_device_farm.types.upload_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "status" in value:
        import capo_device_farm.types.upload_status

        out["status"] = capo_device_farm.types.upload_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "url" in value:
        out["url"] = value["url"]
    if "metadata" in value:
        out["metadata"] = value["metadata"]
    if "content_type" in value:
        out["contentType"] = value["content_type"]
    if "message" in value:
        out["message"] = value["message"]
    if "category" in value:
        import capo_device_farm.types.upload_category

        out["category"] = capo_device_farm.types.upload_category.serialize_aws_json_1_1(
            value["category"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Upload:
    out: Upload = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("created") is not None:
        import capo_device_farm.types.date_time

        out["created"] = capo_device_farm.types.date_time.deserialize_aws_json_1_1(
            data["created"]
        )
    if data.get("type") is not None:
        import capo_device_farm.types.upload_type

        out["type"] = capo_device_farm.types.upload_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if data.get("status") is not None:
        import capo_device_farm.types.upload_status

        out["status"] = capo_device_farm.types.upload_status.deserialize_aws_json_1_1(
            data["status"]
        )
    if data.get("url") is not None:
        out["url"] = data["url"]
    if data.get("metadata") is not None:
        out["metadata"] = data["metadata"]
    if data.get("contentType") is not None:
        out["content_type"] = data["contentType"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("category") is not None:
        import capo_device_farm.types.upload_category

        out["category"] = (
            capo_device_farm.types.upload_category.deserialize_aws_json_1_1(
                data["category"]
            )
        )
    return out


def redact_sensitive(value: Upload) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "url" in value:
        out["url"] = "*** Sensitive Data Redacted ***"
    return out
