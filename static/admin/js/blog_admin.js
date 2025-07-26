
document.addEventListener('DOMContentLoaded', function() {
    // Auto-generar slug desde el título
    const titleField = document.querySelector('#id_title');
    const slugField = document.querySelector('#id_slug');
    
    if (titleField && slugField) {
        titleField.addEventListener('input', function() {
            const title = this.value;
            const slug = title
                .toLowerCase()
                .replace(/[^a-z0-9\s-]/g, '')
                .replace(/\s+/g, '-')
                .replace(/-+/g, '-')
                .trim('-');
            slugField.value = slug;
        });
    }
    
    // Preview de la imagen destacada
    const imageField = document.querySelector('#id_featured_image');
    if (imageField) {
        imageField.addEventListener('change', function() {
            const url = this.value;
            let preview = document.querySelector('.image-preview');
            
            if (!preview) {
                preview = document.createElement('div');
                preview.className = 'image-preview';
                this.parentNode.appendChild(preview);
            }
            
            if (url) {
                preview.innerHTML = `<img src="${url}" style="max-width: 200px; max-height: 150px; border-radius: 8px; margin-top: 10px;" />`;
            } else {
                preview.innerHTML = '';
            }
        });
        
        // Trigger inicial si ya hay URL
        if (imageField.value) {
            imageField.dispatchEvent(new Event('change'));
        }
    }
    
    // Contador de caracteres para excerpt
    const excerptField = document.querySelector('#id_excerpt');
    if (excerptField) {
        const counter = document.createElement('div');
        counter.style.cssText = 'font-size: 12px; color: #666; margin-top: 5px;';
        excerptField.parentNode.appendChild(counter);
        
        function updateCounter() {
            const length = excerptField.value.length;
            counter.textContent = `${length} caracteres (recomendado: 100-160)`;
            counter.style.color = length > 160 ? '#d63384' : length < 100 ? '#fd7e14' : '#198754';
        }
        
        excerptField.addEventListener('input', updateCounter);
        updateCounter();
    }
    
    // Mejorar el editor de contenido con toolbar básico
    const contentField = document.querySelector('#id_content');
    if (contentField) {
        createContentToolbar(contentField);
    }
});

function createContentToolbar(textarea) {
    const toolbar = document.createElement('div');
    toolbar.className = 'content-editor-toolbar';
    
    const buttons = [
        { text: 'B', action: 'bold', title: 'Negrita' },
        { text: 'I', action: 'italic', title: 'Cursiva' },
        { text: 'H1', action: 'h1', title: 'Título 1' },
        { text: 'H2', action: 'h2', title: 'Título 2' },
        { text: 'Link', action: 'link', title: 'Enlace' },
        { text: 'Img', action: 'image', title: 'Imagen' },
    ];
    
    buttons.forEach(btn => {
        const button = document.createElement('button');
        button.type = 'button';
        button.textContent = btn.text;
        button.title = btn.title;
        button.addEventListener('click', () => insertMarkdown(textarea, btn.action));
        toolbar.appendChild(button);
    });
    
    textarea.parentNode.insertBefore(toolbar, textarea);
    textarea.style.borderRadius = '0 0 4px 4px';
}

function insertMarkdown(textarea, action) {
    const start = textarea.selectionStart;
    const end = textarea.selectionEnd;
    const selectedText = textarea.value.substring(start, end);
    let replacement = '';
    
    switch (action) {
        case 'bold':
            replacement = `**${selectedText || 'texto en negrita'}**`;
            break;
        case 'italic':
            replacement = `*${selectedText || 'texto en cursiva'}*`;
            break;
        case 'h1':
            replacement = `# ${selectedText || 'Título 1'}`;
            break;
        case 'h2':
            replacement = `## ${selectedText || 'Título 2'}`;
            break;
        case 'link':
            replacement = `[${selectedText || 'texto del enlace'}](url)`;
            break;
        case 'image':
            replacement = `![${selectedText || 'alt text'}](url_de_imagen)`;
            break;
    }
    
    textarea.value = textarea.value.substring(0, start) + replacement + textarea.value.substring(end);
    textarea.focus();
    textarea.setSelectionRange(start + replacement.length, start + replacement.length);
}
