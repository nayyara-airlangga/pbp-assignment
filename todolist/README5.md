# Assignment 5: Web Design Using HTML, CSS, and CSS Framework

[Link to Site]: https://pbp-web-assignment.herokuapp.com
[site]: https://pbp-web-assignment.herokuapp.com

[Link to Site]

## What's the difference between Inline, Internal, and External CSS? What are the pros and cons of each of them?

Inline CSS is basically adding a `style` attribute to your desired tag and write the needed CSS. It's not great when needing to style many tags which has the same design, but
could help in styling one specific tag. Internal CSS is done by adding a `style` tag inside the `head` tag of an HTML document. It's useful when we need to style a 
page uniquely with its own styles. It is not recommended to be used when needing to style based on a design for multiple pages. This is where External CSS is useful. We store
the styles we want in a `.css` file and add is as a stylesheet `link` inside of the `head` of page. Any HTML document that links the `.css` file will have its styles accessible.
Hence, its usefulness in designing multiple pages at once if they are similar in design. However, it is tedious to add an external CSS if we only want to use it to style
one single tag in only one page.

## HTML5 tags that I know

- `<p>`
    - Represents a paragraph of text.
- `<h1>, <h2>, <h3>, <h4>, <h5>, <h6>`
    - Represents a heading.
    - Depending on the number, it has a hierarchy that defines the scope of each heading.
- `<a>`
    - Anchor tags for links/hyperlink.
- `<input>`
    - An input field to be filled with data.
    - Have different types such as text, radios, checklists, etc.
- `<img>`
    - Used to represent an image/object.

and so on.

## CSS Selectors I know of

- `element`: Select elements that are of the `<element>` tag.
- `.class`: Select elements with the class named `class`.
- `#id`: Select an element with the id of `id`.
- `element:pseudo-class`: Select all `<element>` elements and define a style based on the `pseudo-class` state.

and so on.

## Implementing the checklists

These steps are based of the latest commit of my assignment 4.

1. Add the bootstraps stylesheet CDN link and JS script to the `head` of `base.html`. This ensures all html templates based off of it will have Bootstrap styles.
2. Create a custom CSS stylesheet in `static/css/styles.css`. I like to have more room for customization so that's why I made a custom stylesheet.
3. Add the stylesheet link to the `base.html` head.
4. Modify each `todolist` template using the Bootstrao styles and my custom CSS styles.
5. For responsive design, I didn't use media query as it wasn't necessary for my implementation. Nevertheless, it is good way to implement it in. I used flex and grid
   columns in my own stylesheet and some using Bootstrap. I also used min and max widths and playing around with it. Since it's all card-like, this is enough to achieve
   a responsive design I like.
   
Here is the link to my [site].
