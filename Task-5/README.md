# Task-2

### Made by David Carl & Tjalfe Møller
### www.dcarl.me

See help and guide on how to import data in the assignment [here!](https://github.com/datsoftlyngby/soft2019spring-databases/blob/master/assignments/assignment5.md)

## Exercise 1

> Write a stored procedure `denormalizeComments(postID)` that moves all comments for a post (the parameter) into a json array on the post. 

```
CREATE PROCEDURE denormalizeComments(IN p_postId INT)
BEGIN
    UPDATE posts SET Comments = (
        select JSON_ARRAYAGG(JSON_OBJECT('id', Id, 'score', Score, 'text', Text, 'creationDate', CreationDate, 'userId', userId)) 
        from comments 
        where PostId = p_postId
    ) 
    WHERE Id = p_postId;
END;
```

## Exercise 2

> Create a trigger such that new adding new comments to a post triggers an insertion of that comment in the json array from exercise 1.

```
CREATE TRIGGER after_comments_insert 
    AFTER INSERT ON comments
    FOR EACH ROW 
BEGIN
    CALL denormalizeComments(NEW.PostId);
END
```

## Exercise 3

> Rather than using a trigger, create a stored procedure to add a comment to a post - adding it both to the comment table and the json array

```
CREATE PROCEDURE createComment(IN p_Id INT, IN p_PostId INT, IN p_Score INT, IN p_Text text, IN p_CreationDate DATETIME, IN p_UserId INT)
BEGIN
    INSERT INTO comments (Id, PostId, Score, Text, CreationDate,UserId) values (p_Id, p_PostId, p_Score, p_Text, p_CreationDate, p_UserId);
    CALL denormalizeComments(p_postId);
END;
```