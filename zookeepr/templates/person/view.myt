View person

(<a href="<% h.url_for(action='new') %>">new person</a>)
(<a href="<% h.url_for(action='index') %>">list persons</a>)

(<a href="<% h.url_for(action='edit') %>">edit this person</a>)
(<a href="<% h.url_for(action='delete') %>">delete this person</a>)


% for (label, key) in [('handle', 'handle')]:
<div class="formlabel"><% label %>:</div>
<div class="formfield"><% getattr(c.person, key) %></div>
% #endfor