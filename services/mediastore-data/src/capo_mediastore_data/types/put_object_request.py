"""Generated from Smithy shape ``com.amazonaws.mediastoredata#PutObjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediastore_data.types.content_type
    import capo_mediastore_data.types.path_naming
    import capo_mediastore_data.types.payload_blob
    import capo_mediastore_data.types.storage_class
    import capo_mediastore_data.types.string_primitive
    import capo_mediastore_data.types.upload_availability


class PutObjectRequest(TypedDict, closed=True):
    body: "capo_mediastore_data.types.payload_blob.PayloadBlob"
    """<p>The bytes to be stored. </p>"""
    path: "capo_mediastore_data.types.path_naming.PathNaming"
    r"""<p>The path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name></p> <p>For example, to upload the file <code>mlaw.avi</code> to the folder path <code>premium\canada</code> in the container <code>movies</code>, enter the path <code>premium/canada/mlaw.avi</code>.</p> <p>Do not include the container name in this path.</p> <p>If the path includes any folders that don't exist yet, the service creates them. For example, suppose you have an existing <code>premium/usa</code> subfolder. If you specify <code>premium/canada</code>, the service creates a <code>canada</code> subfolder in the <code>premium</code> folder. You then have two subfolders, <code>usa</code> and <code>canada</code>, in the <code>premium</code> folder. </p> <p>There is no correlation between the path to the source and the path (folders) in the container in AWS Elemental MediaStore.</p> <p>For more information about folders and how they exist in a container, see the <a href="http://docs.aws.amazon.com/mediastore/latest/ug/">AWS Elemental MediaStore User Guide</a>.</p> <p>The file name is the name that is assigned to the file that you upload. The file can have the same name inside and outside of AWS Elemental MediaStore, or it can have the same name. The file name can include or omit an extension. </p>"""
    content_type: NotRequired["capo_mediastore_data.types.content_type.ContentType"]
    """<p>The content type of the object.</p>"""
    cache_control: NotRequired[
        "capo_mediastore_data.types.string_primitive.StringPrimitive"
    ]
    """<p>An optional <code>CacheControl</code> header that allows the caller to control the object's cache behavior. Headers can be passed in as specified in the HTTP at <a href="https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9">https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9</a>.</p> <p>Headers with a custom user-defined value are also accepted.</p>"""
    storage_class: NotRequired["capo_mediastore_data.types.storage_class.StorageClass"]
    """<p>Indicates the storage class of a <code>Put</code> request. Defaults to high-performance temporal storage class, and objects are persisted into durable storage shortly after being received.</p>"""
    upload_availability: NotRequired[
        "capo_mediastore_data.types.upload_availability.UploadAvailability"
    ]
    """<p>Indicates the availability of an object while it is still uploading. If the value is set to <code>streaming</code>, the object is available for downloading after some initial buffering but before the object is uploaded completely. If the value is set to <code>standard</code>, the object is available for downloading only when it is uploaded completely. The default value for this header is <code>standard</code>.</p> <p>To use this header, you must also set the HTTP <code>Transfer-Encoding</code> header to <code>chunked</code>.</p>"""
