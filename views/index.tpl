% rebase('base.tpl')
<b>Available links:</b>
<ul>
    % for link in links:
    <li>(<a href="/{{link.id}}-">stat</a>) <a href="/{{link.id}}">{{link.id}}</a> — <a href="{{link.url}}">{{link.url}}</a></li>
    %end
</ul><br/>
<b>Shorten a new link:</b>
<form action="/" method="POST">
    <input type="hidden" name="action" value="add" />
    URL: <input type="text" name="link_url" placeholder="http://example.com/" />
    <input type="checkbox" name="autodelete" />Delete after first visit<br />
    <input type="submit" value="Add" />
</form><br/>
<b>Delete an existing shortened link:</b>
<form action="/" method="POST">
    <input type="hidden" name="action" value="delete" />
    ID: <input type="text" name="link_id" placeholder="aoB0eVbhPQ" />
    <input type="submit" value="Delete" />
</form><br/>