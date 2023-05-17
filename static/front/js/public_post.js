$(function () {
    // var editor = new window.wangEditor("#editor");
    // editor.create();

    const {createEditor, createToolbar} = window.wangEditor

    const editorConfig = {
        placeholder: 'Type here...',
        onChange(editor) {
            const html = editor.getHtml()
            console.log('editor content', html)
            // 也可以同步到 <textarea>
        }
    }

    const editor = createEditor({
        selector: '#editor-container',
        html: '<p><br></p>',
        config: editorConfig,
        mode: 'default', // or 'simple'
    })

    const toolbarConfig = {}

    const toolbar = createToolbar({
        editor,
        selector: '#toolbar-container',
        config: toolbarConfig,
        mode: 'default', // or 'simple'
    })

    // 修改 uploadImage 菜单配置
    editorConfig.MENU_CONF['uploadImage'] = {
    server: '/upload/image',
    fieldName: 'image'
    // 继续写其他配置...

    //【注意】不需要修改的不用写，wangEditor 会去 merge 当前其他配置
}
})