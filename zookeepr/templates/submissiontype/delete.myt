<%flags>
	inherit="/layout.myt"
</%flags>
<%args>
defaults
errors
</%args>

Delete submission type

<&| MODULE:mylib:formfill, defaults=defaults, errors=errors &>
<form name="delete_subtype" action="<% h.url_for(action='delete') %>" method="post" >

<div class="formlabel">Are you sure?</div>

<input type="hidden" name="delete" value="ok" />

<div class="submit"><input type="submit" value="Delete" /></div>

</form>
</&>