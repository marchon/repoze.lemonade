from zope.interface import Interface
from zope.interface import Attribute
from zope.interface.interfaces import IInterface
from zope.component.interfaces import IObjectEvent

class IContentType(IInterface):
    """ Interface type representing a content type """

class IObjectModifiedEvent(IObjectEvent):
    """ An event type sent when an object is modified """
    object = Attribute('The object being modified')

class IObjectWillBeAddedEvent(IObjectEvent):
    """ An event type sent when an before an object is added """
    object = Attribute('The object being added')
    parent = Attribute('The folder to which the object is being added')
    name = Attribute('The name which the object is being added to the folder '
                     'with')

class IObjectAddedEvent(IObjectEvent):
    """ An event type sent when an object is added """
    object = Attribute('The object being added')
    parent = Attribute('The folder to which the object is being added')
    name = Attribute('The name which the object is being added to the folder '
                     'with')

class IObjectWillBeRemovedEvent(IObjectEvent):
    """ An event type sent before an object is removed """
    object = Attribute('The object being added')
    parent = Attribute('The folder to which the object is being added')
    name = Attribute('The name which the object is being added to the folder '
                     'with')

class IObjectRemovedEvent(IObjectEvent):
    """ An event type sent when an object is removed """
    object = Attribute('The object being added')
    parent = Attribute('The folder to which the object is being added')
    name = Attribute('The name which the object is being added to the folder '
                     'with')

class IContentFactory(Interface):
    """ Content factory """
    def __call__(*arg, **kw):
        """ Return a content instance  """
    
class IFolder(Interface):
    """ Folder """
    def __init__(data=None):
        """ Initialize the folder using ``data`` (should be an OOBTree
        object) or an empty OOBTree object if ``data`` is ``None``."""
    def keys():
        """ Return a ``BTreeItems`` sequence representing the keys
        (object names) present in the folder.  Use list() against this
        value to expand eagerly."""
    def __iter__():
        """ Return an iterator which iterates over the keys in the folder """
    def values():
        """ Return a ``BTreeItems`` sequence representing the values
        (object values) present in the folder. Use list() against this
        value to expand eagerly."""
    def items():
        """ Return a ``BTreeItems`` sequence representing the values
        (object values) present in the folder. Use list() against this
        value to expand eagerly."""
    def get(name, default=None):
        """ Return the object value named by ``name`` or the default
        if the object name does not exist"""
    def __contains__(name):
        """ Return ``True`` if the container contains the object value
        named by name, ``False`` otherwise """
    def __nonzero__():
        """ Always return True """
    def __setitem__(name, other):
        """ Set an object into this folder using the name ``name`` and
        the value ``other``.  ``name`` must be a Unicode or ASCII
        object; if ``name`` is an ASCII object, it must be a 7-bit
        value only.  ``name`` cannot be the empty string.  When
        ``other`` is seated into this folder, it will also be
        decorated with a ``__parent__`` attribute (a reference to the
        folder into which it is being seated) and ``__name__``
        attribute (the name passed in to this function.  If a value
        already exists with the name ``name`` within this folder, it
        will be removed from the container before the new value is
        added.  When this method is called, an
        ``ObjectWillBeAddedEvent`` event will be emitted before the
        object obtains a ``__name__`` or ``__parent__`` value.  After
        the object obtains a ``__name__`` and ``__parent__`` value, an
        ObjecAddedEvent will be emitted."""
    def __delitem__(name):
        """ Delete an object value from this folder that is already
        present in the folder with the name ``name``.  If the object
        value with the name ``name`` does not exist in the folder a
        ``KeyError`` will be raised.  When the object value referred
        to by ``name`` is deleted from this folder, its ``__parent__``
        and ``__name__`` values will be removed from the object.  When
        this method is called, an ``ObjectWillBeRemovedEvent`` event
        will be emitted before the object loses its ``__name__`` or
        ``__parent__`` values.  After the object loses its
        ``__name__`` and ``__parent__`` value, an
        ``ObjectRemovedEvent`` will be emitted."""
        
    

