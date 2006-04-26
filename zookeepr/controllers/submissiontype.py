from zookeepr.lib.base import *

class SubmissiontypeController(BaseController):
    
    def index(self):
        # index action lists
        # GET -> return list of subtypes
        # POST -> NOOP, do GET
        m.write('list subtypes')

    def view(self, id):
        # GET -> return subtype
        # POST -> NOOP, do GET
        m.write('view subtype %s' % id)

    def edit(self, id):
        # GET -> return 'edit' form
        # POST -> update entry with form results
        m.write('edit subtype %s' % id)

    def delete(self, id):
        # GET -> return 'delete' formm
        # POST -> act on results of delete form
        errors, defaults = {}, m.request_args
        #h.log(defaults)
        if defaults:
            #h.log(defaults)
            st = model.SubmissionType.get(id)
            st.delete()
            st.commit()
            return h.redirect_to(action='index', id=None)
        m.subexec('submissiontype/delete.myt', defaults=defaults, errors=errors)

    def new(self):
        # GET -> return 'new' form
        # POST -> create new with results of form
        errors, defaults = {}, m.request_args
        if defaults:
            # create, etc
            st = model.SubmissionType(**defaults)

            # put in db
            st.commit()

            # redirect to.. somewhere
            return h.redirect_to(action='view', id=st.id)
        
        m.subexec('submissiontype/new.myt', defaults=defaults, errors=errors)