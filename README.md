# SPECIAL_DJANGO

## Themes
- Pagination

Porpirétés et Methodes

        # quelques proprietes et fonctions
          . class Paginator(object_list, per_page, orphans=0, allow_empty_first_page=True) # 
          . Paginator.count # Le nombre total d’objets sur toutes les pages.
          . Paginator.num_pages #Le nombre total de pages.
          . Paginator.page_range # Une itération d’intervalle de numéros de pages commençant à 1, 
                                  par ex. produisant [1, 2, 3, 4].
       
           Exceptions InvalidPage  
            . exception PageNotAnInteger
            . exception EmptyPage
            
            Methodes
            . Page.has_next() # Renvoie True s’il existe une page suivante.
            . Page.has_previous() # Renvoie True s’il existe une page précédente.
            . Page.has_other_pages() # Renvoie True s’il existe une page suivante ou. une page précédente.
            . Page.next_page_number() # Renvoie le prochain numéro de page. 
                                        Génère InvalidPage s’il n’y a pas de page suivante.
            . Page.previous_page_number() # Renvoie le numéro de page précédent. 
                                         Génère InvalidPage s’il n’y a pas de page précédente.
            . Page.start_index() : Renvoie l’index (commençant par 1) du premier objet de la page, 
                                relatif à tous les autres objets de la liste du paginateur. Par exemple,*
                                lors de la pagination d’une liste de 5 objets par groupes de 2, la méthode 
                                start_index() de la deuxième page renverrait 3.
              . Page.end_index() : Contrairement a start_index return l'index du dernier lement de la page
              
              
              Attributs
                . Page.object_list # La liste des objets de cette page.
                . Page.number # Le numéro de page (commençant par 1) de cette page.
                . Page.paginator # Le numéro de page (commençant par 1) de cette page.

 views.py
 
        from django.core.paginator import Paginator
        from django.shortcuts import render
        def listing(request):
            contact_list = Contacts.objects.all()
            paginator = Paginator(contact_list, 25) # Show 25 contacts per page

            page = request.GET.get('page')
            contacts = paginator.get_page(page)
            return render(request, 'list.html', {'contacts': contacts})
           
           
  list.html
  
          {% for contact in contacts %}
              {# Each "contact" is a Contact model object. #}
              {{ contact.full_name|upper }}<br>
              ...
          {% endfor %}

            <div class="pagination">
                <span class="step-links">
                    {% if contacts.has_previous %}
                        <a href="?page=1">&laquo; first</a>
                        <a href="?page={{ contacts.previous_page_number }}">previous</a>
                    {% endif %}

                    <span class="current">
                        Page {{ contacts.number }} of {{ contacts.paginator.num_pages }}.
                    </span>

                    {% if contacts.has_next %}
                        <a href="?page={{ contacts.next_page_number }}">next</a>
                        <a href="?page={{ contacts.paginator.num_pages }}">last &raquo;</a>
                    {% endif %}
                </span>
             </div>
             
          
## Liens
Partgage d'artticle sur les resau sociaux: https://pypi.org/project/django-social-share/
